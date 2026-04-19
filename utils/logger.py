import json

LOG_FILE = "audit_log.json"

def log(ticket_id, step, data):
    entry = {
        "ticket_id": ticket_id,
        "step": step,
        "data": data
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)