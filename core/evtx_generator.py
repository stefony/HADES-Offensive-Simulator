import os

def generate_evtx_script(event_data, output_path="logs/generate_event.ps1"):
    os.makedirs("logs", exist_ok=True)

    command = f"""
    $EventID = 4688
    $Message = "Process {event_data.get('sysmon', {}).get('new_process', 'cmd.exe')} created from {event_data.get('sysmon', {}).get('parent_process', 'explorer.exe')}"
    $Time = Get-Date
    Write-EventLog -LogName "Application" -Source "HADES-Simulator" -EventID $EventID -EntryType Information -Message $Message
    """

    with open(output_path, "w") as f:
        f.write(command.strip())

    print(f"[+] PowerShell script written to: {output_path}")
    print("[!] Run as Administrator to inject into Event Viewer.")
