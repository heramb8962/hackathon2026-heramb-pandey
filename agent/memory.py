memory_store = []

def store(ticket, result):
    memory_store.append({
        "message": ticket["message"],
        "result": result
    })

def get_similar(message):
    for item in memory_store:
        if message.lower() in item["message"].lower():
            return item["result"]
    return None

def get_similar(message):
    msg = message.lower()

    for item in memory_store:
        if any(word in item["message"].lower() for word in msg.split()):
            return item["result"]

    return None