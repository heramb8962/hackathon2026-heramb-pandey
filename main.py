from tools.order import get_order
from utils.retry import retry

result = retry(lambda: get_order("ORD123"))

print(result)