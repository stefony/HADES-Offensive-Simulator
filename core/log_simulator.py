import json
import os

def generate_log(event_dict, output_path="logs/event_log.json"):
    os.makedirs("logs", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(event_dict, f, indent=4)
    print("[+] Simulated log written to:", output_path)
