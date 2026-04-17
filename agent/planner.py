def plan(ticket):
    """
    Decide steps based on ticket message
    """

    message = ticket["message"].lower()

    print(f"[PLANNER] Planning for: {message}")

    if "refund" in message or "damaged" in message:
        return [
            "get_order",
            "check_refund",
            "issue_refund",
            "send_reply"
        ]
    
    elif "where" in message or "status" in message:
        return [
            "get_order",
            "send_reply"
        ]
    
    else:
        return [
            "send_reply"
        ]