from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from utils.retry import retry

order = retry(lambda: get_order("ORD123"))

eligibility = retry(lambda: check_refund_eligibility(order))

if eligibility["eligible"]:
    refund = retry(lambda: issue_refund("ORD123", order["amount"]))
    print("Refund:", refund)
else:
    print("Not eligible:", eligibility)