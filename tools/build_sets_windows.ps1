$ErrorActionPreference = 'Stop'
$taskRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$taskBuild = Join-Path $taskRoot 'build\sets'
$taskResolvedBuild = [IO.Path]::GetFullPath($taskBuild)
# Build output must stay within the production boundary specified by this task.
if (-not $taskResolvedBuild.StartsWith(($taskRoot.TrimEnd('\') + '\'), [StringComparison]::OrdinalIgnoreCase)) { throw 'Build directory outside repo boundary' }
$taskMutex = [Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
$taskAcquired = $false
$taskAbandoned = $false
Add-Type -TypeDefinition @'
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
try {
    try { $taskAcquired = $taskMutex.WaitOne(120000) }
    catch [Threading.AbandonedMutexException] { $taskAcquired = $true; $taskAbandoned = $true }
    if (-not $taskAcquired) { throw 'TeX mutex acquisition timed out after 120000 ms; no TeX launched' }
    $taskPassResults = @()
    Push-Location $taskResolvedBuild
    try {
        for ($taskPass = 1; $taskPass -le 2; $taskPass++) {
            $taskJob = [BengaliTexJob]::CreateJobObject([IntPtr]::Zero,$null)
            $taskProcess = [Diagnostics.Process]::new()
            $taskProcess.StartInfo.FileName = (Get-Command xelatex -ErrorAction Stop).Source
            $taskProcess.StartInfo.Arguments = '--disable-installer -no-shell-escape -interaction=nonstopmode -halt-on-error openlogic-bn-sets.tex'
            $taskProcess.StartInfo.WorkingDirectory = $taskResolvedBuild
            $taskProcess.StartInfo.UseShellExecute = $false
            $taskProcess.StartInfo.CreateNoWindow = $true
            $taskProcess.StartInfo.RedirectStandardOutput = $true
            $taskProcess.StartInfo.RedirectStandardError = $true
            $taskProcess.StartInfo.Environment['SOURCE_DATE_EPOCH'] = '1788520000'
            $taskProcess.StartInfo.Environment['FORCE_SOURCE_DATE'] = '1'
            try {
                [void]$taskProcess.Start()
                if (-not [BengaliTexJob]::AssignProcessToJobObject($taskJob,$taskProcess.Handle)) { $taskProcess.Kill($true); $taskProcess.WaitForExit(); throw 'Cannot capture TeX process tree in job' }
                $taskStdout = $taskProcess.StandardOutput.ReadToEndAsync()
                $taskStderr = $taskProcess.StandardError.ReadToEndAsync()
                if (-not $taskProcess.WaitForExit(90000)) { [void][BengaliTexJob]::TerminateJobObject($taskJob,124); $taskProcess.WaitForExit(); throw 'Captured TeX tree exceeded 90-second bound' }
                while ([BengaliTexJob]::Active($taskJob) -gt 0) { [Threading.Thread]::Sleep(100) }
                $taskCode = $taskProcess.ExitCode
                $taskOutput = $taskStdout.GetAwaiter().GetResult() + $taskStderr.GetAwaiter().GetResult()
            } catch { [void][BengaliTexJob]::TerminateJobObject($taskJob,125); if (-not $taskProcess.HasExited) { $taskProcess.WaitForExit() }; throw }
            finally { [void][BengaliTexJob]::CloseHandle($taskJob); $taskProcess.Dispose() }
            $taskSanitized = $taskOutput.Replace($env:USERPROFILE,'[PROFILE]')
            [IO.File]::WriteAllText((Join-Path $taskResolvedBuild "pass-$taskPass.txt"),$taskSanitized)
            $taskPdfPath = Join-Path $taskResolvedBuild 'openlogic-bn-sets.pdf'
            $taskPdfHash = if (Test-Path -LiteralPath $taskPdfPath) { (Get-FileHash -Algorithm SHA256 -LiteralPath $taskPdfPath).Hash.ToLowerInvariant() } else { $null }
            $taskPassResults += @{pass=$taskPass;exit_code=$taskCode;pdf_sha256=$taskPdfHash}
            if ($taskCode -ne 0) { throw "TeX pass $taskPass failed with exit code $taskCode" }
        }
        $taskLogPath = Join-Path $taskResolvedBuild 'openlogic-bn-sets.log'
        $taskLog = [IO.File]::ReadAllText($taskLogPath).Replace($env:USERPROFILE,'[PROFILE]')
        [IO.File]::WriteAllText($taskLogPath,$taskLog)
        $taskFindings = @($taskLog -split "`n" | Where-Object { $_ -match 'Missing character|Overfull|undefined|LaTeX Error' })
        $taskReceipt = @{mutex='Global\InterlanguageTeXSlotV1';acquisition_timeout_ms=120000;acquired=$true;abandoned_recovery=$taskAbandoned;passes=$taskPassResults;stable_pdf_between_passes=($taskPassResults[0].pdf_sha256 -eq $taskPassResults[1].pdf_sha256);log_findings=$taskFindings;tree_policy='Captured Windows job; parent and descendants end before pass completion. Shell escape and installer disabled; mutex spans both passes and immediate log checks.'}
        $taskReceipt | ConvertTo-Json -Depth 5
    } finally { Pop-Location }
} finally {
    if ($taskAcquired) { $taskMutex.ReleaseMutex() }
    $taskMutex.Dispose()
}
