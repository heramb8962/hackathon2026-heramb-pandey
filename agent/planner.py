from agent.llm import llm_plan
import ast


def fix_plan(steps, message):
    msg = message.lower()

    # Remove refund steps if not needed
    if not any(word in msg for word in ["refund", "damaged", "broken", "wrong", "defective"]):
        steps = [s for s in steps if s not in ["check_refund", "issue_refund"]]

    if ("check_refund" in steps or "issue_refund" in steps) and "get_order" not in steps:
        steps.insert(0, "get_order")

    ordered = []

    if "get_order" in steps:
        ordered.append("get_order")

    if "check_refund" in steps:
        ordered.append("check_refund")

    if "issue_refund" in steps:
        ordered.append("issue_refund")

    if "search_kb" in steps:
        ordered.append("search_kb")

    if "send_reply" not in ordered:
        ordered.append("send_reply")

    return ordered


def plan(ticket):
    message = ticket["message"]
    msg = message.lower()

    print("[PLANNER] Using improved planner")

    # ✅ PRIORITY 1: KNOWLEDGE BASE (VERY IMPORTANT)
    if any(w in msg for w in ["policy", "how", "cancel", "exchange", "delivery", "help"]):
        steps = ["search_kb", "send_reply"]

    # ✅ PRIORITY 2: REFUND / RETURN ACTION
    elif any(w in msg for w in ["refund", "return", "damaged", "broken", "wrong", "defective"]):
        steps = ["get_order", "check_refund", "issue_refund", "send_reply"]

    # ✅ PRIORITY 3: ORDER TRACKING
    elif any(w in msg for w in ["where", "track", "status", "arrived", "package"]):
        steps = ["get_order", "send_reply"]

    # ✅ DEFAULT
    else:
        steps = ["get_order", "send_reply"]

    print(f"[PLANNER] Final Plan: {steps}")
    return steps