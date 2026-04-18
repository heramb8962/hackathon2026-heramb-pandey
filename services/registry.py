from tools.order import get_order
from tools.refund import check_refund_eligibility, issue_refund
from tools.kb import search_kb

SERVICES = {
    "get_order": get_order,
    "check_refund": check_refund_eligibility,
    "issue_refund": issue_refund,
    "search_kb": search_kb
}