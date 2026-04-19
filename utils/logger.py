import json
import os

AUDIT_FILE = "audit_log.json"

def log_audit(entry):
    data = []

    # ✅ If file exists and is valid → load
    if os.path.exists(AUDIT_FILE):
        try:
            with open(AUDIT_FILE, "r") as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
        except:
            data = []  # corrupted file → reset

    # ✅ append new entry
    data.append(entry)

    # ✅ write safely
    with open(AUDIT_FILE, "w") as f:
        json.dump(data, f, indent=2)