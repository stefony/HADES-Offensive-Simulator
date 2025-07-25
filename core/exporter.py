import csv
import os


def flatten_dict(d, parent_key='', sep='_'):
    """
    Recursively flattens a nested dictionary.
    Example:
    {"a": {"b": 1}} → {"a_b": 1}
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def export_to_csv(json_event, output_file="logs/export.csv"):
    """
    Exports a (possibly nested) JSON event to flat CSV.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    flat_event = flatten_dict(json_event)

    with open(output_file, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_event.keys())
        writer.writeheader()
        writer.writerow(flat_event)

    print(f"[+] Exported event to CSV: {output_file}")
