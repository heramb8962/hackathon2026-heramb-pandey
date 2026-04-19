from agent.planner import plan
from agent.executor_async import execute_async
from agent.memory import store, get_similar
from utils.metrics import start, end
from agent.response_generator import generate_reply
from utils.logger import log_audit

import re

def extract_order_id(message):
    match = re.search(r"ORD\d+", message.upper())
    return match.group(0) if match else None


def get_priority(msg):
    msg = msg.lower()
    if any(word in msg for word in ["urgent", "asap", "immediately"]):
        return "HIGH"
    if any(word in msg for word in ["refund", "damaged", "broken", "wrong"]):
        return "MEDIUM"
    return "LOW"


def decide(results):
    if "error" in results:
        return "escalate", 0.2

    if "eligibility" in results:
        if not results["eligibility"].get("eligible", True):
            return "escalate", 0.5

    if "refund" in results and results["refund"].get("status") == "success":
        return "resolved", 0.95

    return "resolved", 0.85


def self_reflect(results):
    if "error" in results:
        return "Agent failed due to tool/service error and escalated."
    if "refund" in results:
        return "Agent successfully processed refund after validating eligibility."
    if "order" in results:
        return "Agent fetched order details and responded successfully."
    return "Agent handled the query successfully."


def detect_anomaly(ticket):
    print("[ANOMALY] Suspicious input detected")

    return {
        "results": {
            "reply": "⚠️ We couldn't understand your request. Please provide more details."
        },
        "decision": "escalate",
        "confidence": 0.2,
        "priority": "LOW",
        "reflection": "Agent detected anomalous or unclear input."
    }


async def process_ticket(ticket):
    if not ticket.get("order_id"):
        extracted = extract_order_id(message)
        if extracted:
            ticket["order_id"] = extracted

    print(f"\n[AGENT] Processing {ticket.get('ticket_id', 'N/A')}")

    message = ticket.get("message", "").lower()

    # 🔺 priority
    priority = get_priority(message)
    print(f"[PRIORITY] {priority}")

    # 🚨 anomaly
    if detect_anomaly(ticket):
        print("[ANOMALY] Suspicious input detected")

    # 🧠 MEMORY (STRICT MATCH ONLY)
    past = get_similar(message)
    if past:
        print("[MEMORY] Reusing past solution")
        return past

    # ⏱️ metrics start
    t0 = start()

    # 🧠 planning
    steps = plan(ticket)

    # ⚙️ execution
    results = await execute_async(steps, ticket)

    print("DEBUG RESULTS:", results)  # 🔥 keep for verification

    # ⏱️ metrics end
    end(t0, success=("error" not in results))

    # 🧠 decision
    decision, confidence = decide(results)

    # 🧠 reply (ALWAYS AFTER EXECUTION)
    results["reply"] = generate_reply(results, ticket)

    # 🚨 escalation override
    if decision == "escalate":
        results["reply"] = (
            "⚠️ We couldn't fully process your request. "
            "It has been forwarded to a human agent."
        )

    reflection = self_reflect(results)

    final_output = {
        "results": results,
        "decision": decision,
        "confidence": confidence,
        "priority": priority,
        "reflection": reflection
    }

    store(ticket, final_output)

    print(f"[AGENT] Decision: {decision} (confidence: {confidence})")

    log_audit({
    "ticket_id": ticket.get("ticket_id"),
    "message": ticket.get("message"),
    "steps": results.get("steps_executed", []),
    "decision": decision,
    "confidence": confidence,
    "priority": priority,
    "output": results
    })

    return final_output