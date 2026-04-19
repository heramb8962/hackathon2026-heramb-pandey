def generate_reply(results, ticket):
    message = ticket.get("message", "").lower()

    # 🚨 ERROR CASE (highest priority)
    if "error" in results:
        return (
            "⚠️ We couldn't process your request due to a temporary issue. "
            "Our support team has been notified."
        )

    # 💰 REFUND SUCCESS
    if "refund" in results and results["refund"].get("status") == "success":
        amount = results["refund"]["amount"]
        return f"✅ Your refund of ₹{amount} has been successfully processed."

    # ❌ REFUND NOT ELIGIBLE
    if "eligibility" in results:
        if not results["eligibility"].get("eligible", True):
            return (
                "⚠️ Your request is not eligible for a refund. "
                "Our support team can assist you further."
            )

    # 📚 KNOWLEDGE BASE
    if "kb" in results and results["kb"].get("answer"):
        return f"ℹ️ {results['kb']['answer']}"

    # 📦 ORDER STATUS (AFTER refund checks!)
    if "order" in results:
        status = results["order"]["status"]

        if status == "shipped":
            return "📦 Your order has been shipped and is on the way."

        elif status == "delivered":
            # differentiate intent
            if "refund" in message or "damaged" in message:
                return "📦 Your order was delivered. Let me help you with your refund request."
            return "📦 Your order has been delivered successfully."

        else:
            return f"📦 Your order status is '{status}'."

    # 🧠 INTENT-BASED FALLBACK
    if "refund" in message:
        return "⚠️ We are reviewing your refund request."

    if "order" in message:
        return "📦 We are checking your order details."

    confidence = results.get("confidence", 0)

    if confidence < 0.5:
        return "⚠️ I'm not fully confident. Escalating to human agent."
    
    return "✅ Your request has been processed successfully."