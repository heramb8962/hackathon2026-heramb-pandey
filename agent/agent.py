from agent.planner import plan
from agent.executor import execute

def decide(results):
    """
    Decide final outcome
    """

    if "error" in results:
        return "escalate", 0.3

    if "eligibility" in results:
        if not results["eligibility"]["eligible"]:
            return "escalate", 0.5

    return "resolved", 0.9


def process_ticket(ticket):
    print(f"\n[AGENT] Processing ticket {ticket['ticket_id']}")

    steps = plan(ticket)

    results = execute(steps, ticket)

    decision, confidence = decide(results)

    print(f"[AGENT] Decision: {decision} (confidence: {confidence})")

    return {
        "results": results,
        "decision": decision,
        "confidence": confidence
    }