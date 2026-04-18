def plan(ticket):
    print("[PLANNER] Using Intelligent Rule-Based Planner...")

    message = ticket["message"].lower()

    steps = []

    # Step 1: Always fetch order if order_id exists
    if "order_id" in ticket:
        steps.append("get_order")

    # Step 2: Detect intent
    if any(word in message for word in ["refund", "damaged", "broken"]):
        steps.append("check_refund")
        steps.append("issue_refund")
    
    elif any(word in message for word in ["where", "status", "track"]):
        # only need order info
        pass
    
    elif any(word in message for word in ["wrong item", "replacement"]):
        steps.append("check_refund")

    # Step 3: Always reply
    steps.append("send_reply")

    print(f"[PLANNER] Final Plan: {steps}")

    return steps