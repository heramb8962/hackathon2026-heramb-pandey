import json

with open("data/kb.json") as f:
    KB = json.load(f)

def search_kb(message):
    msg = message.lower()
    for item in KB:
        if item["q"] in msg:
            return {"answer": item["a"]}
    return {"answer": None}