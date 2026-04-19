import random

ORDERS_DB = {
    "ORD123": {"status": "delivered", "amount": 1200},
    "ORD124": {"status": "shipped", "amount": 800},
    "ORD125": {"status": "delivered", "amount": 1500},
}


def get_order(order_id):
    print(f"[TOOL] Fetching order {order_id}...")

    # ❌ invalid order
    if order_id not in ORDERS_DB:
        raise Exception("Invalid order ID")

    # simulate occasional failure
    if random.random() < 0.1:
        raise Exception("Order service timeout")

    return ORDERS_DB[order_id]