import asyncio
from config import RETRY_COUNT, RETRY_DELAY

async def async_retry(func):
    for i in range(RETRY_COUNT):
        try:
            return await func()
        except Exception as e:
            print(f"[RETRY] {i+1}: {e}")
            await asyncio.sleep(RETRY_DELAY)

    return {"error": "All retries failed"}