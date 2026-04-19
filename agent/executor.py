import asyncio
from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund

async def execute_streaming(steps, ticket):
    results = {"steps_executed": []}

    for step in steps:
        yield step, None  # 🔥 tell UI step started

        try:
            if step == "get_order":
                data = get_order(ticket["order_id"])
                results["order"] = data

            elif step == "check_refund":
                data = check_refund_eligibility(results["order"])
                results["eligibility"] = data

            elif step == "issue_refund":
                if results["eligibility"]["eligible"]:
                    data = issue_refund(
                        ticket["order_id"],
                        results["order"]["amount"]
                    )
                    results["refund"] = data

            elif step == "send_reply":
                results["reply"] = "Processing..."

            results["steps_executed"].append(step)

            yield step, results  # 🔥 send update to UI

            await asyncio.sleep(0.5)

        except Exception as e:
            results["error"] = str(e)
            yield "error", results
            break