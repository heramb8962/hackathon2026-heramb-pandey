from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from utils.retry import retry

def execute(plan, ticket):
    """
    Execute steps one by one
    """

    print(f"[EXECUTOR] Executing plan: {plan}")

    results = {}

    for step in plan:
        try:
            if step == "get_order":
                results["order"] = retry(lambda: get_order(ticket["order_id"]))

            elif step == "check_refund":
                results["eligibility"] = retry(
                    lambda: check_refund_eligibility(results["order"])
                )

            elif step == "issue_refund":
                if results["eligibility"]["eligible"]:
                    results["refund"] = retry(
                        lambda: issue_refund(
                            ticket["order_id"],
                            results["order"]["amount"]
                        )
                    )

            elif step == "send_reply":
                results["reply"] = "Your request has been processed."

        except Exception as e:
            print(f"[ERROR] {e}")
            results["error"] = str(e)
            break

    return results