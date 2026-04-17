import json
from datetime import datetime

def log(ticket_id, step, data):
    entry = {
        "timestamp": str(datetime.now()),
        "ticket_id": ticket_id,
        "step": step,
        "data": data
    }

    with open("audit_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")