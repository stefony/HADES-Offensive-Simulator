import os


def generate_evtx_script(event_data, output_path="logs/generate_event.ps1"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    sysmon = event_data.get("sysmon", {})

    # Default values if sysmon is missing
    new_proc = sysmon.get("new_process", event_data.get("tool", "cmd.exe"))
    parent_proc = sysmon.get("parent_process", "explorer.exe")
    attack_name = event_data.get("attack", "Unknown Attack")
    timestamp = event_data.get("timestamp", "N/A")
    event_id = event_data.get("event_id", "0000-0000")

    # PowerShell command template
    command = f"""
    $EventID = 4688
    $Source = "HADES-Simulator"
    $Message = "Simulated Event: {attack_name} → Process {new_proc} spawned from {parent_proc} at {timestamp} [event_id: {event_id}]"
    $Time = Get-Date
    if (-not (Get-EventLog -LogName Application -Source $Source -ErrorAction SilentlyContinue)) {{
        New-EventLog -LogName Application -Source $Source
    }}
    Write-EventLog -LogName "Application" -Source $Source -EventID $EventID -EntryType Information -Message $Message
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(command.strip())

    print(f"[+] PowerShell script written to: {output_path}")
    print("[!] Run as Administrator to inject into Event Viewer.")
