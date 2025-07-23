$EventID = 4688
    $Message = "Process powershell.exe created from explorer.exe"
    $Time = Get-Date
    Write-EventLog -LogName "Application" -Source "HADES-Simulator" -EventID $EventID -EntryType Information -Message $Message