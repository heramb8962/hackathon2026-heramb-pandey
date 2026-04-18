memory = []

def store(ticket, result):
    memory.append({
        "ticket": ticket["message"],
        "result": result
    })

def get_similar(message):
    for item in memory:
        if message.lower() in item["ticket"].lower():
            return item["result"]
    return None