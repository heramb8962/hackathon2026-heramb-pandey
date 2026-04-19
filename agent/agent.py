from agent.planner import plan
from agent.executor_async import execute_async
from agent.memory import store, get_similar
from utils.metrics import start, end
from agent.response_generator import generate_reply


# 🔺 PRIORITY DETECTION
def get_priority(msg):
    msg = msg.lower()

    if any(word in msg for word in ["urgent", "asap", "immediately"]):
        return "HIGH"

    if any(word in msg for word in ["refund", "damaged", "broken", "wrong"]):
        return "MEDIUM"

    return "LOW"


# 🧠 DECISION ENGINE
def decide(results):
    if "error" in results:
        return "escalate", 0.2

    if "eligibility" in results:
        if not results["eligibility"].get("eligible", True):
            return "escalate", 0.5

    if "refund" in results and results["refund"].get("status") == "success":
        return "resolved", 0.95

    return "resolved", 0.85


# 🧠 SELF-REFLECTION
def self_reflect(results):
    if "error" in results:
        return "Agent failed due to tool/service error and escalated."

    if "refund" in results:
        return "Agent successfully processed refund after validating eligibility."

    if "order" in results:
        return "Agent fetched order details and responded successfully."

    return "Agent handled the query successfully."


# 🚨 ANOMALY DETECTION
def detect_anomaly(ticket):
    msg = ticket.get("message", "").lower()
    return len(msg) < 5 or "asdf" in msg


# ✅ MAIN ASYNC FUNCTION
async def process_ticket(ticket):
    print(f"\n[AGENT] Processing {ticket.get('ticket_id', 'N/A')}")

    message = ticket.get("message", "")

    # 🔺 PRIORITY
    priority = get_priority(message)
    print(f"[PRIORITY] {priority}")

    # 🚨 ANOMALY CHECK
    if detect_anomaly(ticket):
        print("[ANOMALY] Suspicious input detected")

    # 🧠 MEMORY CHECK (STRICT MATCH)
    past = get_similar(message)
    if past:
        print("[MEMORY] Reusing past solution")
        return past

    # ⏱️ START METRICS
    t0 = start()

    # 🧠 PLANNING
    steps = plan(ticket)

    # ⚙️ EXECUTION
    results = await execute_async(steps, ticket)

    # ⏱️ END METRICS
    end(t0, success=("error" not in results))

    # 🧠 DECISION
    decision, confidence = decide(results)

    # 🧠 GENERATE SMART REPLY (🔥 CRITICAL FIX)
    results["reply"] = generate_reply(results, ticket)

    # 🚨 OVERRIDE REPLY IF ESCALATED
    if decision == "escalate":
        results["reply"] = (
            "⚠️ We couldn't fully process your request. "
            "It has been forwarded to a human agent."
        )

    # 🧠 REFLECTION
    reflection = self_reflect(results)

    final_output = {
        "results": results,
        "decision": decision,
        "confidence": confidence,
        "priority": priority,
        "reflection": reflection
    }

    # 💾 STORE IN MEMORY
    store(ticket, final_output)

    print(f"[AGENT] Decision: {decision} (confidence: {confidence})")

    return final_output