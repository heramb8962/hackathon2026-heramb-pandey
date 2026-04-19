def generate_reply(results, ticket):
    message = ticket.get("message", "").lower()

    if "error" in results and "Invalid order ID" in results["error"]:
        return "⚠️ The order ID you provided is invalid. Please check and try again."
    
    if len(message.strip()) < 5:
        return "⚠️ Please provide more details so we can assist you better."

    # ERROR
    if "error" in results:
        return "⚠️ We couldn't process your request. It has been forwarded to a human agent."

    # 📚 KB HAS HIGHER PRIORITY
    if "kb" in results:
        return f"ℹ️ {results['kb']['answer']}"
    
    # REFUND
    if "refund" in results and any(w in message for w in ["refund", "damaged", "broken", "wrong", "defective"]):
        refund = results["refund"]
        if refund.get("status") == "success":
            return f"✅ Your refund of ₹{refund['amount']} has been successfully processed."

    # NOT ELIGIBLE
    if "eligibility" in results and not results["eligibility"].get("eligible", True):
        return "⚠️ Your request is not eligible for a refund."

    # KB
    if "kb" in results:
        return f"ℹ️ {results['kb']['answer']}"

    # ORDER
    if "order" in results:
        status = results["order"]["status"]

        if status == "shipped":
            return "📦 Your order has been shipped and is on the way."

        if status == "delivered":
            if any(w in message for w in ["refund", "return", "damaged", "broken"]):
                return "📦 Your order was delivered. We are checking your return/refund request."
            return "📦 Your order has been delivered successfully."

    # FALLBACK
    return "✅ Your request has been processed successfully."