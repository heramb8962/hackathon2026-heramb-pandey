memory_store = []

def store(ticket, result):
    memory_store.append({
        "message": ticket["message"].lower(),
        "result": result
    })

def get_similar(message):
    msg = message.lower()

    for item in memory_store:
        if msg == item["message"]:   # 🔥 STRICT MATCH ONLY
            return item["result"]

    return None