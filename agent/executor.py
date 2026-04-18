from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from utils.retry import retry
from utils.logger import log

def execute(plan, ticket):
    print(f"[EXECUTOR] Executing plan: {plan}")

    results = {"steps_executed": []}

    for step in plan:
        try:
            results["steps_executed"].append(step)

            # 🔹 GET ORDER
            if step == "get_order":
                result = retry(lambda: get_order(ticket["order_id"]))

                if "error" in result:
                    results["error"] = result["error"]
                    break

                results["order"] = result
                log(ticket["ticket_id"], "get_order", result)

            # 🔹 CHECK REFUND
            elif step == "check_refund":
                if "order" not in results:
                    results["error"] = "Order missing"
                    break

                result = retry(lambda: check_refund_eligibility(results["order"]))

                if "error" in result:
                    results["error"] = result["error"]
                    break

                results["eligibility"] = result
                log(ticket["ticket_id"], "check_refund", result)

            # 🔹 ISSUE REFUND
            elif step == "issue_refund":
                if not results.get("eligibility", {}).get("eligible", False):
                    continue

                result = retry(
                    lambda: issue_refund(
                        ticket["order_id"],
                        results["order"]["amount"]
                    )
                )

                if "error" in result:
                    results["error"] = result["error"]
                    break

                results["refund"] = result
                log(ticket["ticket_id"], "issue_refund", result)

            # 🔹 SEND REPLY
            elif step == "send_reply":
                if "error" in results:
                    reply = "⚠️ Unable to process automatically. Escalated to human agent."
                elif "refund" in results:
                    reply = "✅ Refund processed successfully."
                elif "eligibility" in results and not results["eligibility"]["eligible"]:
                    reply = "⚠️ Not eligible for refund. Escalating."
                else:
                    reply = "📦 Request processed successfully."

                results["reply"] = reply
                log(ticket["ticket_id"], "send_reply", reply)

        except Exception as e:
            print(f"[ERROR] {e}")
            results["error"] = str(e)
            log(ticket["ticket_id"], "error", str(e))
            break

    return results