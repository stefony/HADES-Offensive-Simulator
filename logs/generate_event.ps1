$EventID = 4688
    $Source = "HADES-Simulator"
    $Message = "Simulated Event: Credential Dump → Process Mimikatz spawned from explorer.exe at 2025-07-26T12:19:49.175157 [event_id: 2ad27c8b-0713-4696-b957-7a56b6b19b2f]"
    $Time = Get-Date
    if (-not (Get-EventLog -LogName Application -Source $Source -ErrorAction SilentlyContinue)) {
        New-EventLog -LogName Application -Source $Source
    }
    Write-EventLog -LogName "Application" -Source $Source -EventID $EventID -EntryType Information -Message $Message