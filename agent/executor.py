from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from utils.retry import retry
from utils.logger import log

def execute(plan, ticket):
    print(f"[EXECUTOR] Executing plan: {plan}")

    results = {}

    for step in plan:
        try:
            if step == "get_order":
                results["order"] = retry(lambda: get_order(ticket["order_id"]))
                log(ticket["ticket_id"], "get_order", results["order"])

            elif step == "check_refund":
                results["eligibility"] = retry(
                    lambda: check_refund_eligibility(results["order"])
                )
                log(ticket["ticket_id"], "check_refund", results["eligibility"])

            elif step == "issue_refund":
                if results["eligibility"]["eligible"]:
                    results["refund"] = retry(
                        lambda: issue_refund(
                            ticket["order_id"],
                            results["order"]["amount"]
                        )
                    )
                    log(ticket["ticket_id"], "issue_refund", results["refund"])

            elif step == "send_reply":
                results["reply"] = "Your request has been processed."
                log(ticket["ticket_id"], "send_reply", results["reply"])

        except Exception as e:
            print(f"[ERROR] {e}")
            results["error"] = str(e)
            log(ticket["ticket_id"], "error", str(e))
            break

    return results