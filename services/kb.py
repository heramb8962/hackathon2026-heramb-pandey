def search_kb(query):
    q = query.lower()

    if "cancel" in q:
        return {"answer": "You can cancel your order from the orders section before it is shipped."}

    if "return policy" in q:
        return {"answer": "You can return products within 7 days of delivery."}

    if "exchange" in q:
        return {"answer": "Exchange is available for eligible products within 7 days."}

    if "delivery" in q:
        return {"answer": "Delivery usually takes 3-5 business days."}

    if "refund process" in q:
        return {"answer": "Refunds are processed within 5-7 business days after approval."}

    return {"answer": "Please contact support for more details."}