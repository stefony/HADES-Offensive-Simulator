import csv
import os

def export_to_csv(json_event, output_file="logs/export.csv"):
    os.makedirs("logs", exist_ok=True)
    flat_event = {}

    for k, v in json_event.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                flat_event[f"{k}_{sub_k}"] = sub_v
        else:
            flat_event[k] = v

    with open(output_file, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_event.keys())
        writer.writeheader()
        writer.writerow(flat_event)

    print(f"[+] Exported event to CSV: {output_file}")
