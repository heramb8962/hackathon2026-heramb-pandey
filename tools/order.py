import random
import time

def get_order(order_id):
    """
    Simulates fetching order details from a database/service
    Includes:
    - random delay
    - random failure
    """

    print(f"[TOOL] Fetching order {order_id}...")

    # simulate network delay
    time.sleep(random.uniform(0.5, 1.5))

    # simulate failure (20% chance)
    if random.random() < 0.2:
        raise Exception("Order service timeout")

    # mock database
    orders = {
        "ORD123": {"status": "delivered", "amount": 1200},
        "ORD124": {"status": "shipped", "amount": 800},
        "ORD125": {"status": "delivered", "amount": 1500},
    }

    order = orders.get(order_id)

    if not order:
        raise Exception("Order not found")

    print(f"[TOOL] Order fetched: {order}")

    return order