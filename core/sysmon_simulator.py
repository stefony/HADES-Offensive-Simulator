import random
import uuid
import time

def generate_sysmon_4688(process_name, parent_process, cmdline):
    event = {
        "event_id": 4688,
        "record_id": random.randint(1000, 9999),
        "time_generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "process_guid": str(uuid.uuid4()),
        "parent_process": parent_process,
        "new_process": process_name,
        "command_line": cmdline,
        "integrity_level": "Medium",
        "detected": random.choice([True, False]),
        "detection_note": "Suspicious PowerShell reverse shell detected" if "powershell" in cmdline.lower() else "N/A"
    }
    return event
