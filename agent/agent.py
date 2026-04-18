from agent.planner import plan
from agent.executor import execute
from agent.memory import store, get_similar

def decide(results):
    if "error" in results:
        return "escalate", 0.3

    if "eligibility" in results:
        if not results["eligibility"]["eligible"]:
            return "escalate", 0.5

    confidence = 0.9 if "refund" in results else 0.8
    return "resolved", confidence


def process_ticket(ticket):
    print(f"\n[AGENT] Processing ticket {ticket['ticket_id']}")

    # 🔹 Memory check
    past = get_similar(ticket["message"])
    if past:
        print("[MEMORY] Found similar case, reusing result")
        return past

    # 🔹 Planning
    steps = plan(ticket)

    # 🔹 Execution
    results = execute(steps, ticket)

    # 🔹 Decision
    decision, confidence = decide(results)

    final = {
        "results": results,
        "decision": decision,
        "confidence": confidence
    }

    # 🔹 Store memory
    store(ticket, final)

    print(f"[AGENT] Decision: {decision} (confidence: {confidence})")

    return final