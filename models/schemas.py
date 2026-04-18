from pydantic import BaseModel
from typing import Dict, Any

class Ticket(BaseModel):
    ticket_id: int
    message: str
    order_id: str
    email: str

class Result(BaseModel):
    results: Dict[str, Any]
    decision: str
    confidence: float
    priority: str
    reflection: str