import time

METRICS = {"total": 0, "success": 0, "errors": 0, "latencies": []}

def start():
    return time.time()

def end(start_time, success=True):
    METRICS["total"] += 1
    METRICS["latencies"].append(time.time() - start_time)

    if success:
        METRICS["success"] += 1
    else:
        METRICS["errors"] += 1