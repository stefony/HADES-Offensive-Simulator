from time import sleep
from colorama import Fore
from core.sysmon_simulator import generate_sysmon_4688


def simulate_credential_dump():
    print(Fore.RED + "[*] Simulating credential dumping using mimikatz...")
    sleep(1)
    print(Fore.YELLOW + "sekurlsa::logonpasswords")
    sleep(1)
    print(Fore.GREEN + "[+] Dump complete.")
    return {
        "attack": "Credential Dumping",
        "tool": "Mimikatz",
        "technique": "T1003.001",
        "timestamp": "2025-07-23 14:00:00"
    }
def simulate_reverse_shell():
    print(Fore.RED + "[*] Simulating reverse shell...")
    sleep(1)
    
    attacker_ip = "192.168.1.66"
    attacker_port = 4444

    # Simulated obfuscated payload (base64 encoded PowerShell)
    payload = "cG93ZXJzaGVsbC5leGUgLW5vcGAgLUNvbW1hbmQgJ2Jhc2gtaSA+ICRudWxsID4gJjEn"
    decoded_cmd = "powershell.exe -nop -Command 'bash -i > $null 2>&1'"
    
    print(Fore.YELLOW + f"Encoded payload: {payload}")
    sleep(1)

    sysmon_event = generate_sysmon_4688("powershell.exe", "explorer.exe", decoded_cmd)

    print(Fore.GREEN + "[+] Reverse shell launched (simulated).")

    return {
        "attack": "Reverse Shell",
        "technique": "T1059.001",
        "obfuscation": "base64 encoded payload",
        "payload": payload,
        "source_ip": attacker_ip,
        "dest_port": attacker_port,
        "stealth_score": 7.5,
        "timestamp": sysmon_event["time_generated"],
        "sysmon": sysmon_event
    }

