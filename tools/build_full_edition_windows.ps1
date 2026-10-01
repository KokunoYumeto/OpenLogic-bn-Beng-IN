$Edition='full-edition'
$ErrorActionPreference = 'Stop'
$taskRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$taskBuild = Join-Path $taskRoot ('build\' + $Edition)
$taskBase = 'openlogic-bn-Beng-IN-complete'
$taskResolvedBuild = [IO.Path]::GetFullPath($taskBuild)
# Build output must stay within the production boundary specified by this task.
if (-not $taskResolvedBuild.StartsWith(($taskRoot.TrimEnd('\') + '\'), [StringComparison]::OrdinalIgnoreCase)) { throw 'Build directory outside repo boundary' }
$taskMutex = [Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
$taskAcquired = $false
$taskAbandoned = $false
$taskAttemptPath = Join-Path $taskResolvedBuild ('attempt-' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff') + '.json')
$taskRecord = @{edition=$Edition;status='starting';mutex='Global\InterlanguageTeXSlotV1';acquisition_timeout_ms=0;input_sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $taskResolvedBuild ($taskBase + '.tex'))).Hash.ToLowerInvariant();started_utc=[DateTime]::UtcNow.ToString('o');acquired=$false}
[IO.File]::WriteAllText($taskAttemptPath,($taskRecord | ConvertTo-Json -Depth 6))
if (-not ('BengaliTexJob' -as [type])) { Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
public class BengaliTexJob {
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode)] public static extern IntPtr CreateJobObject(IntPtr a,string name);
 [DllImport("kernel32.dll")] public static extern bool AssignProcessToJobObject(IntPtr j,IntPtr p);
 [DllImport("kernel32.dll", SetLastError=true)] public static extern bool QueryInformationJobObject(IntPtr j,int c,IntPtr p,uint n,IntPtr r);
 [DllImport("kernel32.dll")] public static extern bool TerminateJobObject(IntPtr j,uint code);
 [DllImport("kernel32.dll")] public static extern bool CloseHandle(IntPtr h);
 public static int Active(IntPtr j) { IntPtr p=Marshal.AllocHGlobal(48); try { if(!QueryInformationJobObject(j,1,p,48,IntPtr.Zero)) throw new Exception("Cannot query captured TeX job: " + Marshal.GetLastWin32Error()); return Marshal.ReadInt32(p,40); } finally {Marshal.FreeHGlobal(p);} }
}
'@
}
try {
    try { $taskAcquired = $taskMutex.WaitOne(0) }
    catch [Threading.AbandonedMutexException] { $taskAcquired = $true; $taskAbandoned = $true }
    if (-not $taskAcquired) {
        $taskRecord.status='deferred_tex_slot'
        $taskRecord['reason']='TeX slot occupied; retain pending build and continue substantive work. No TeX launched.'
        $taskRecord | ConvertTo-Json -Depth 6
        return
    }
    $taskRecord.acquired=$true
    $taskRecord['abandoned_recovery']=$taskAbandoned
    $taskPassResults = @()
    $taskBibtexResult = $null
    $taskStable = $false
    $taskMetadataOutput = & python -X utf8 (Join-Path $PSScriptRoot 'edition_metadata.py')
    if ($LASTEXITCODE -ne 0) { throw 'Cannot read current edition metadata' }
    $taskMetadata = $taskMetadataOutput | ConvertFrom-Json
    $taskRecord['edition_identity']=$taskMetadata
    Push-Location $taskResolvedBuild
    try {
        for ($taskPass = 1; $taskPass -le 5; $taskPass++) {
            $taskJob = [BengaliTexJob]::CreateJobObject([IntPtr]::Zero,$null)
            $taskProcess = [Diagnostics.Process]::new()
            $taskProcess.StartInfo.FileName = (Get-Command xelatex -ErrorAction Stop).Source
            $taskProcess.StartInfo.Arguments = '--disable-installer -no-shell-escape -interaction=nonstopmode -halt-on-error ' + $taskBase + '.tex'
            $taskProcess.StartInfo.WorkingDirectory = $taskResolvedBuild
            $taskProcess.StartInfo.UseShellExecute = $false
            $taskProcess.StartInfo.CreateNoWindow = $true
            $taskProcess.StartInfo.RedirectStandardOutput = $true
            $taskProcess.StartInfo.RedirectStandardError = $true
            $taskProcess.StartInfo.Environment['SOURCE_DATE_EPOCH'] = $taskMetadata.source_date_epoch
            $taskProcess.StartInfo.Environment['FORCE_SOURCE_DATE'] = '1'
            try {
                $taskDeadline = [DateTime]::UtcNow.AddSeconds(300)
                [void]$taskProcess.Start()
                if (-not [BengaliTexJob]::AssignProcessToJobObject($taskJob,$taskProcess.Handle)) { $taskProcess.Kill($true); $taskProcess.WaitForExit(); throw 'Cannot capture TeX process tree in job' }
                $taskStdout = $taskProcess.StandardOutput.ReadToEndAsync()
                $taskStderr = $taskProcess.StandardError.ReadToEndAsync()
                if (-not $taskProcess.WaitForExit(300000)) { [void][BengaliTexJob]::TerminateJobObject($taskJob,124); $taskProcess.WaitForExit(); throw 'Captured TeX tree exceeded 300-second bound' }
                while ([BengaliTexJob]::Active($taskJob) -gt 0) { if ([DateTime]::UtcNow -gt $taskDeadline) { [void][BengaliTexJob]::TerminateJobObject($taskJob,124); throw 'Captured TeX descendants exceeded 300-second bound' }; [Threading.Thread]::Sleep(100) }
                $taskCode = $taskProcess.ExitCode
                $taskOutput = $taskStdout.GetAwaiter().GetResult() + $taskStderr.GetAwaiter().GetResult()
            } catch { [void][BengaliTexJob]::TerminateJobObject($taskJob,125); if (-not $taskProcess.HasExited) { $taskProcess.WaitForExit() }; throw }
            finally { [void][BengaliTexJob]::CloseHandle($taskJob); $taskProcess.Dispose() }
            $taskSanitized = $taskOutput.Replace($env:USERPROFILE,'[PROFILE]')
            [IO.File]::WriteAllText((Join-Path $taskResolvedBuild "pass-$taskPass.txt"),$taskSanitized)
            $taskPdfPath = Join-Path $taskResolvedBuild ($taskBase + '.pdf')
            $taskPdfHash = if (Test-Path -LiteralPath $taskPdfPath) { (Get-FileHash -Algorithm SHA256 -LiteralPath $taskPdfPath).Hash.ToLowerInvariant() } else { $null }
            $taskPassResults += @{pass=$taskPass;exit_code=$taskCode;pdf_sha256=$taskPdfHash}
            if ($taskCode -ne 0) { throw "TeX pass $taskPass failed with exit code $taskCode" }
            if ($taskPass -eq 1) {
                # BibTeX is a separate captured process tree under the same mutex.
                $taskBibJob = [BengaliTexJob]::CreateJobObject([IntPtr]::Zero,$null)
                $taskBibProcess = [Diagnostics.Process]::new()
                $taskBibProcess.StartInfo.FileName = (Get-Command bibtex -ErrorAction Stop).Source
                $taskBibProcess.StartInfo.Arguments = $taskBase + '.aux'
                $taskBibProcess.StartInfo.WorkingDirectory = $taskResolvedBuild
                $taskBibProcess.StartInfo.UseShellExecute = $false
                $taskBibProcess.StartInfo.CreateNoWindow = $true
                $taskBibProcess.StartInfo.RedirectStandardOutput = $true
                $taskBibProcess.StartInfo.RedirectStandardError = $true
                $taskBibProcess.StartInfo.Environment['MIKTEX_ENABLE_INSTALLER'] = '0'
                try {
                    $taskBibDeadline = [DateTime]::UtcNow.AddSeconds(300)
                    [void]$taskBibProcess.Start()
                    if (-not [BengaliTexJob]::AssignProcessToJobObject($taskBibJob,$taskBibProcess.Handle)) { $taskBibProcess.Kill($true); $taskBibProcess.WaitForExit(); throw 'Cannot capture BibTeX process tree in job' }
                    $taskBibStdout = $taskBibProcess.StandardOutput.ReadToEndAsync()
                    $taskBibStderr = $taskBibProcess.StandardError.ReadToEndAsync()
                    if (-not $taskBibProcess.WaitForExit(300000)) { [void][BengaliTexJob]::TerminateJobObject($taskBibJob,124); $taskBibProcess.WaitForExit(); throw 'Captured BibTeX tree exceeded 300-second bound' }
                    while ([BengaliTexJob]::Active($taskBibJob) -gt 0) { if ([DateTime]::UtcNow -gt $taskBibDeadline) { [void][BengaliTexJob]::TerminateJobObject($taskBibJob,124); throw 'Captured BibTeX descendants exceeded 300-second bound' }; [Threading.Thread]::Sleep(100) }
                    $taskBibCode = $taskBibProcess.ExitCode
                    $taskBibOutput = $taskBibStdout.GetAwaiter().GetResult() + $taskBibStderr.GetAwaiter().GetResult()
                } catch { [void][BengaliTexJob]::TerminateJobObject($taskBibJob,125); if (-not $taskBibProcess.HasExited) { $taskBibProcess.WaitForExit() }; throw }
                finally { [void][BengaliTexJob]::CloseHandle($taskBibJob); $taskBibProcess.Dispose() }
                [IO.File]::WriteAllText((Join-Path $taskResolvedBuild 'bibtex.txt'),$taskBibOutput.Replace($env:USERPROFILE,'[PROFILE]'))
                $taskBibtexResult = @{exit_code=$taskBibCode;output_sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $taskResolvedBuild 'bibtex.txt')).Hash.ToLowerInvariant()}
                if ($taskBibCode -ne 0) { throw "BibTeX failed with exit code $taskBibCode" }
            }
            if ($taskPass -ge 3 -and $taskPassResults[-1].pdf_sha256 -eq $taskPassResults[-2].pdf_sha256) { $taskStable = $true; break }
        }
        if (-not $taskStable) { throw 'PDF did not converge within five guarded TeX passes' }
        $taskLogPath = Join-Path $taskResolvedBuild ($taskBase + '.log')
        $taskLog = [IO.File]::ReadAllText($taskLogPath).Replace($env:USERPROFILE,'[PROFILE]')
        [IO.File]::WriteAllText($taskLogPath,$taskLog)
        $taskFindings = @($taskLog -split "`n" | Where-Object { $_ -match 'Missing character|Overfull|undefined|LaTeX Error' })
        $taskReceipt = @{mutex='Global\InterlanguageTeXSlotV1';acquisition_timeout_ms=0;acquired=$true;abandoned_recovery=$taskAbandoned;passes=$taskPassResults;bibtex=$taskBibtexResult;stable_pdf_between_passes=$taskStable;log_findings=$taskFindings;tree_policy='Captured Windows jobs; each TeX/BibTeX parent and descendants end before the next pass. Shell escape and installer disabled; mutex spans all passes and immediate log checks.'}
        $taskReceipt | ConvertTo-Json -Depth 5
        $taskRecord['build']=$taskReceipt
        $taskRecord.status='completed'
    } finally { Pop-Location }
} catch {
    $taskRecord.status='failed'
    $taskRecord['error']=$_.Exception.Message.Replace($env:USERPROFILE,'[PROFILE]')
    throw
} finally {
    if ($taskAcquired) { $taskMutex.ReleaseMutex() }
    $taskMutex.Dispose()
    $taskRecord['ended_utc']=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText($taskAttemptPath,($taskRecord | ConvertTo-Json -Depth 6))
    [IO.File]::WriteAllText((Join-Path $taskResolvedBuild 'latest-attempt.json'),($taskRecord | ConvertTo-Json -Depth 6))
}
