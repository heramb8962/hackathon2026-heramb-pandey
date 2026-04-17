import random
import time

def check_refund_eligibility(order):
    """
    Checks if an order is eligible for refund
    """

    print("[TOOL] Checking refund eligibility...")

    time.sleep(random.uniform(0.3, 1.0))

    # simulate occasional failure
    if random.random() < 0.1:
        raise Exception("Refund service unavailable")

    if order["status"] == "delivered":
        return {
            "eligible": True,
            "reason": "Delivered item eligible for refund (e.g., damaged)"
        }
    
    return {
        "eligible": False,
        "reason": "Order not delivered yet"
    }


def issue_refund(order_id, amount):
    """
    Simulates issuing refund
    """

    print(f"[TOOL] Issuing refund for {order_id}...")

    time.sleep(random.uniform(0.5, 1.2))

    if random.random() < 0.1:
        raise Exception("Payment gateway error")

    return {
        "status": "success",
        "order_id": order_id,
        "amount": amount
    }