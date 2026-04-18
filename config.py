import os

RETRY_COUNT = int(os.getenv("RETRY_COUNT", 3))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", 1))