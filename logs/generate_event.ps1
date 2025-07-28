$EventID = 4688
    $Source = "HADES-Simulator"
    $Message = "Simulated Event: Insecure Deserialization → Process cmd.exe spawned from explorer.exe at N/A [event_id: 0000-0000]"
    $Time = Get-Date
    if (-not (Get-EventLog -LogName Application -Source $Source -ErrorAction SilentlyContinue)) {
        New-EventLog -LogName Application -Source $Source
    }
    Write-EventLog -LogName "Application" -Source $Source -EventID $EventID -EntryType Information -Message $Message