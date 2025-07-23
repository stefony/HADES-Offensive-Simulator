import random
import uuid
import time
import os

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

def generate_sysmon_log(event_dict, output_path="logs/sysmon_log.xml"):
    os.makedirs("logs", exist_ok=True)

    sysmon_template = f"""<Event>
    <System>
        <Provider Name="Microsoft-Windows-Sysmon"/>
        <EventID>1</EventID>
    </System>
    <EventData>
        {"".join([f"<Data Name='{k}'>{v}</Data>" for k, v in event_dict.items()])}
    </EventData>
</Event>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(sysmon_template)

    print("[+] Sysmon log written to:", output_path)
