import asyncio
from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from services.kb import search_kb  # make sure this exists

async def execute_async(steps, ticket):
    results = {"steps_executed": []}

    for step in steps:
        try:
            print(f"[EXECUTOR] Running step: {step}")

            # ---------------- GET ORDER ----------------
            if step == "get_order":
                order_id = ticket.get("order_id")

                if not order_id:
                    raise Exception("Missing order_id")

                try:
                    results["order"] = get_order(order_id)
                except Exception as e:
                    if "Invalid order ID" in str(e):
                        raise Exception("Invalid order ID provided")
                    raise

            # ---------------- CHECK REFUND ----------------
            elif step == "check_refund":
                if "order" not in results:
                    raise Exception("Order missing")

                results["eligibility"] = check_refund_eligibility(
                    results["order"]
                )

            # ---------------- ISSUE REFUND ----------------
            elif step == "issue_refund":
                if results.get("eligibility", {}).get("eligible"):
                    results["refund"] = issue_refund(
                        ticket["order_id"],
                        results["order"]["amount"]
                    )
                else:
                    print("[INFO] Not eligible → skipping refund")

            # ---------------- SEND REPLY ----------------
            elif step == "send_reply":
                pass

            elif step == "search_kb":
                results["kb"] = search_kb(ticket["message"])

            results["steps_executed"].append(step)
            await asyncio.sleep(0.1)

        except Exception as e:
            print(f"[ERROR] {e}")
            results["error"] = str(e)
            results["failed_step"] = step
            break

    return results