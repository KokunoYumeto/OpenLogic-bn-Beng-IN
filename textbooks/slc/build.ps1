[CmdletBinding()]
param([switch]$Cumulative)
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$source = Join-Path $root 'source'
$attempt = Join-Path $root ('.build/' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff'))
$tree = Join-Path $attempt 'source'
$book = Join-Path $tree 'locale/bn/courses/sets-logic-computation'
$receipt = [ordered]@{status='preparing';acquired=$false;commands=@();cumulative=[bool]$Cumulative}
$null = New-Item -ItemType Directory -Path $attempt -Force
Copy-Item -LiteralPath $source -Destination $tree -Recurse
if ($Cumulative) {
    Copy-Item -LiteralPath (Join-Path $root 'slc-screen-bn.tex') -Destination (Join-Path $book 'slc-screen.tex') -Force
}

Add-Type -Path (Join-Path $root 'WindowsProcessJob.cs')
$mutex = [Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
$oldEnv = @{}
foreach ($name in ('BSTINPUTS','SOURCE_DATE_EPOCH','FORCE_SOURCE_DATE','MIKTEX_ENABLEINSTALLER')) {
    $oldEnv[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
}
function Invoke-Captured([string]$Name, [string[]]$Arguments) {
    $exe = (Get-Command $Name -CommandType Application).Source
    $sequence = $receipt.commands.Count + 1
    $stdout = Join-Path $attempt ('{0:d2}-{1}.txt' -f $sequence, $Name)
    $job = [SlcProcessJob]::CreateJobObject([IntPtr]::Zero, $null)
    if ($job -eq [IntPtr]::Zero) { throw 'Windows job creation failed.' }
    $proc = $null
    try {
        $proc = [SlcProcessJob]::Launch($exe, ($Arguments -join ' '), $book, $job, $stdout)
        $watch = [Diagnostics.Stopwatch]::StartNew()
        while (-not $proc.HasExited -or [SlcProcessJob]::Active($job) -gt 0) {
            if ($watch.Elapsed.TotalSeconds -gt 300) { throw "$Name exceeded its five-minute process limit." }
            Start-Sleep -Milliseconds 100
        }
        $proc.WaitForExit()
        $code = $proc.ExitCode
    } finally {
        if ([SlcProcessJob]::Active($job) -gt 0) {
            $null = [SlcProcessJob]::TerminateJobObject($job, 125)
            while ([SlcProcessJob]::Active($job) -gt 0) { Start-Sleep -Milliseconds 100 }
        }
        $null = [SlcProcessJob]::CloseHandle($job)
        if ($proc) { $proc.Dispose() }
    }
    $receipt.commands += @{name=$Name;exit_code=$code;log=(Split-Path -Leaf $stdout)}
    if ($code -ne 0 -or $null -eq $code) { throw "$Name failed. See $stdout." }
}
try {
    try { $receipt.acquired = $mutex.WaitOne(0) }
    catch [Threading.AbandonedMutexException] { $receipt.acquired = $true }
    if (-not $receipt.acquired) {
        $receipt.status = 'slot_occupied'
        Write-Output 'TeX slot occupied; no compiler started.'
        return
    }
    $receipt.status = 'running'
    $env:BSTINPUTS = (Join-Path $tree 'bib') + [IO.Path]::PathSeparator
    $env:SOURCE_DATE_EPOCH = '1794528000'
    $env:FORCE_SOURCE_DATE = '1'
    $env:MIKTEX_ENABLEINSTALLER = '0'
    $version = & xelatex --version | Select-Object -First 1
    $receipt.engine = $version
    $miktex = if ($version -match 'MiKTeX') { @('--disable-installer') } else { @() }
    $tex = @($miktex) + @('-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','slc-screen.tex')
    $bib = @($miktex) + @('slc-screen')
    $ind = @('-s','slc-screen.ist','-t','slc-screen.glg','-o','slc-screen.gls','slc-screen.glo')
    Invoke-Captured xelatex $tex
    Invoke-Captured bibtex $bib
    Invoke-Captured makeindex $ind
    $prior = ''
    for ($pass=2; $pass -le 6; $pass++) {
        Invoke-Captured xelatex $tex
        $hash = (Get-FileHash -LiteralPath (Join-Path $book 'slc-screen.pdf') -Algorithm SHA256).Hash.ToLowerInvariant()
        $log = Get-Content -LiteralPath (Join-Path $book 'slc-screen.log') -Raw -Encoding utf8
        $dirty = $log -match '(?im)There were undefined (?:references|citations)|(?:Reference|Citation) [^\r\n]{0,200} undefined|Label\(s\) may have changed|Rerun to get (?:cross-references|outlines) right|multiply defined|Token [^\r\n]{0,200} undefined|requested but not marked bn|Missing character:'
        if ($pass -eq 2) {
            Invoke-Captured bibtex $bib
            Invoke-Captured makeindex $ind
        } elseif (!$dirty -and $prior -eq $hash) {
            $receipt.pdf_sha256 = $hash
            $receipt.status = 'built'
            break
        }
        $prior = $hash
    }
    if ($receipt.status -ne 'built') { throw 'The screen PDF did not converge with a clean reference and glyph check.' }
} catch {
    $receipt.status = 'failed'
    $receipt.error = $_.Exception.Message
    throw
} finally {
    if ($receipt.acquired) { $mutex.ReleaseMutex() }
    $mutex.Dispose()
    foreach ($name in $oldEnv.Keys) { [Environment]::SetEnvironmentVariable($name, $oldEnv[$name], 'Process') }
    $receipt | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $attempt 'build.json') -Encoding utf8
}
$arguments = @((Join-Path $root 'check-build.py'),$book)
if ($Cumulative) { $arguments += '--cumulative' }
& python -X utf8 @arguments
if ($LASTEXITCODE -ne 0) { throw 'The textbook inventory did not pass.' }
$name = if ($Cumulative) { 'slc-screen-bn-cumulative.pdf' } else { 'slc-screen-bn.pdf' }
Copy-Item -LiteralPath (Join-Path $book 'slc-screen.pdf') -Destination (Join-Path $root $name) -Force
Write-Output (Join-Path $root $name)
