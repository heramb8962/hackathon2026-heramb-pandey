import asyncio
from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund


async def execute_async(steps, ticket):
    results = {
        "steps_executed": []
    }

    for step in steps:
        try:
            print(f"[EXECUTOR] Running step: {step}")

            # ---------------- GET ORDER ----------------
            if step == "get_order":
                order_id = ticket.get("order_id")

                if not order_id:
                    raise Exception("Missing order_id")

                # 🔁 retry logic
                for attempt in range(2):
                    try:
                        results["order"] = get_order(order_id)
                        break
                    except Exception as e:
                        print(f"[RETRY] get_order attempt {attempt+1}: {e}")
                        await asyncio.sleep(0.2)
                else:
                    raise Exception("Order service failed after retries")

            # ---------------- CHECK REFUND ----------------
            elif step == "check_refund":
                if "order" not in results:
                    raise Exception("Order data missing before refund check")

                for attempt in range(2):
                    try:
                        results["eligibility"] = check_refund_eligibility(
                            results["order"]
                        )
                        break
                    except Exception as e:
                        print(f"[RETRY] check_refund attempt {attempt+1}: {e}")
                        await asyncio.sleep(0.2)
                else:
                    raise Exception("Refund service failed after retries")

            # ---------------- ISSUE REFUND ----------------
            elif step == "issue_refund":
                if "eligibility" not in results:
                    raise Exception("Eligibility not checked")

                if results["eligibility"].get("eligible"):
                    for attempt in range(2):
                        try:
                            results["refund"] = issue_refund(
                                ticket["order_id"],
                                results["order"]["amount"]
                            )
                            break
                        except Exception as e:
                            print(f"[RETRY] issue_refund attempt {attempt+1}: {e}")
                            await asyncio.sleep(0.2)
                    else:
                        raise Exception("Refund processing failed after retries")
                else:
                    results["refund"] = {
                        "status": "failed",
                        "reason": "Not eligible"
                    }

            # ---------------- SEND REPLY ----------------
            elif step == "send_reply":
                # ❌ DO NOT generate reply here
                # Just mark step as done
                pass

            # ---------------- TRACK STEP ----------------
            results["steps_executed"].append(step)

            await asyncio.sleep(0.1)

        except Exception as e:
            print(f"[EXECUTOR ERROR] Step '{step}' failed: {e}")

            results["error"] = str(e)
            results["failed_step"] = step
            results["steps_executed"].append(step)

            break

    return results