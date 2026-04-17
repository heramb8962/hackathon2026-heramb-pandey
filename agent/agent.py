from agent.planner import plan
from agent.executor import execute

def process_ticket(ticket):
    print(f"\n[AGENT] Processing ticket {ticket['ticket_id']}")

    steps = plan(ticket)

    results = execute(steps, ticket)

    print(f"[AGENT] Result: {results}")

    return results