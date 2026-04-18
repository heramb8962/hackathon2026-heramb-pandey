from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from utils.retry import retry
from utils.logger import log

def execute(plan, ticket):
    print(f"[EXECUTOR] Executing plan: {plan}")

    results = {}

    for step in plan:
        try:
            # 🔹 Fetch order
            if step == "get_order":
                results["order"] = retry(lambda: get_order(ticket["order_id"]))
                log(ticket["ticket_id"], "get_order", results["order"])

            # 🔹 Check refund eligibility
            elif step == "check_refund":
                if "order" not in results:
                    raise Exception("Order data missing before refund check")

                results["eligibility"] = retry(
                    lambda: check_refund_eligibility(results["order"])
                )
                log(ticket["ticket_id"], "check_refund", results["eligibility"])

            # 🔹 Issue refund
            elif step == "issue_refund":
                if not results.get("eligibility", {}).get("eligible", False):
                    print("[EXECUTOR] Refund not eligible, skipping...")
                    continue

                results["refund"] = retry(
                    lambda: issue_refund(
                        ticket["order_id"],
                        results["order"]["amount"]
                    )
                )
                log(ticket["ticket_id"], "issue_refund", results["refund"])

            # 🔹 Send reply (SMART RESPONSE)
            elif step == "send_reply":
                if "refund" in results:
                    reply = "✅ Your refund has been successfully processed."
                elif "eligibility" in results and not results["eligibility"]["eligible"]:
                    reply = "⚠️ Your request is not eligible for refund. Escalating to support."
                else:
                    reply = "📦 Your request has been processed. Please check your order details."

                results["reply"] = reply
                log(ticket["ticket_id"], "send_reply", reply)

        except Exception as e:
            print(f"[ERROR] {e}")
            results["error"] = str(e)
            log(ticket["ticket_id"], "error", str(e))
            break

    return results