import json
import os

def generate_log(event_dict, output_path="logs/event_log.json"):
    os.makedirs("logs", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(event_dict, f, indent=4)
    print("[+] Simulated log written to:", output_path)

def generate_csv_log(event_dict, output_path="logs/export.csv"):
    import csv

    os.makedirs("logs", exist_ok=True)

    with open(output_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(event_dict.keys())
        writer.writerow(event_dict.values())

    print("[+] CSV log written to:", output_path)
