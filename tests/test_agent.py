from agent.agent import process_ticket

def test_basic():
    t = {
        "ticket_id": 1,
        "message": "refund damaged",
        "order_id": "ORD123",
        "email": "test@test.com"
    }

    result = process_ticket(t)
    assert "decision" in result