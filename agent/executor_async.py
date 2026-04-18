from utils.async_retry import async_retry
from tools.async_wrappers import call_tool

async def execute_async(plan, ticket):
    results = {"steps_executed": []}

    for step in plan:
        results["steps_executed"].append(step)

        if step == "get_order":
            res = await async_retry(lambda: call_tool("get_order", ticket["order_id"]))
            if "error" in res:
                results["error"] = res["error"]
                break
            results["order"] = res

        elif step == "check_refund":
            res = await async_retry(lambda: call_tool("check_refund", results["order"]))
            results["eligibility"] = res

        elif step == "issue_refund":
            res = await async_retry(
                lambda: call_tool("issue_refund", ticket["order_id"], results["order"]["amount"])
            )
            results["refund"] = res

        elif step == "search_kb":
            res = await async_retry(lambda: call_tool("search_kb", ticket["message"]))
            results["kb"] = res

        elif step == "send_reply":
            results["reply"] = "Processed successfully"

    return results