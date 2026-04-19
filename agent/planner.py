from agent.llm import llm_plan
import ast

def fix_plan(steps):
    """
    Ensure logical correctness of plan
    """

    # If refund steps exist → ensure get_order first
    if "check_refund" in steps or "issue_refund" in steps:
        if "get_order" not in steps:
            steps.insert(0, "get_order")

    # Ensure order: get_order → check_refund → issue_refund
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

    print("[PLANNER] Trying LLM planner...")

    raw = llm_plan(message)

    if raw:
        try:
            start = raw.find("[")
            end = raw.rfind("]") + 1

            if start != -1 and end != -1:
                cleaned = raw[start:end]

                steps = ast.literal_eval(cleaned)

                valid_steps = {
                    "get_order",
                    "check_refund",
                    "issue_refund",
                    "search_kb",
                    "send_reply"
                }

                steps = [s for s in steps if s in valid_steps]

                # 🔥 FIX PLAN HERE
                steps = fix_plan(steps)

                print(f"[PLANNER] LLM Plan (fixed): {steps}")
                return steps

        except Exception as e:
            print(f"[PLANNER] LLM parsing failed: {e}")

    # 🔁 FALLBACK
    print("[PLANNER] Using fallback planner")

    msg = message.lower()
    steps = ["get_order"]

    if any(word in msg for word in ["refund", "damaged", "broken", "wrong"]):
        steps += ["check_refund", "issue_refund"]

    elif any(word in msg for word in ["how", "can i", "help"]):
        steps = ["search_kb"]

    steps.append("send_reply")

    print(f"[PLANNER] Final Plan: {steps}")
    return steps