from agent.planner import plan
from agent.executor_async import execute_async
from utils.metrics import start, end

def get_priority(msg):
    msg = msg.lower()
    if "urgent" in msg:
        return "HIGH"
    if "refund" in msg:
        return "MEDIUM"
    return "LOW"

def decide(results):
    if "error" in results:
        return "escalate", 0.2
    return "resolved", 0.9


# ✅ NOW ASYNC
async def process_ticket(ticket):
    print(f"\n[AGENT] Processing {ticket['ticket_id']}")

    priority = get_priority(ticket["message"])

    t0 = start()

    steps = plan(ticket)

    # ✅ FIX: directly await
    results = await execute_async(steps, ticket)

    end(t0, success=("error" not in results))

    decision, confidence = decide(results)

    return {
        "results": results,
        "decision": decision,
        "confidence": confidence,
        "priority": priority
    }