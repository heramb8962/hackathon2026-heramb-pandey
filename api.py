from fastapi import FastAPI
from agent.agent import process_ticket

app = FastAPI()

@app.post("/process")
def process(ticket: dict):
    return process_ticket(ticket)

@app.get("/health")
def health():
    return {"status": "ok"}