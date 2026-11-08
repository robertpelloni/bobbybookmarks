# Standing rule: keep heavyweight user apps at BelowNormal so the system never hangs.  
# Allowlist only - never touches System/Defender/audio/shell/diagnostics.  
# Run manually or via Scheduled Task LowerHeavyweightPriority (logon + every 5 min).  
$allow = @('ChatGPT','codex','llama-server','node','python','pythonw','ffmpeg','ffprobe','jules-autopilot','hypernexus','msedge','mpc-hc64','foobar2000','Telegram','UniGetUI','WindowsPackageManagerServer','BingWallpaper','ollama','codewhale','jcode')  
$changed = 0  
foreach ($p in Get-Process) {  
  try {  
    if ($allow -contains $p.Name) {  
      $pc = $p.PriorityClass  
      if ($pc -eq 'Normal' -or $pc -eq 'AboveNormal' -or $pc -eq 'High') {  
        $p.PriorityClass = 'BelowNormal'  
        $changed++  
      }  
    }  
  } catch { }  
}  
Write-Host ('lower-priority done, changed=' + $changed)  
