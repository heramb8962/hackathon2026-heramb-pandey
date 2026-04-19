# ⚠️ Failure Modes Analysis

## 1. Tool Failure (Order Service Timeout)

### Problem:
Order API may fail due to timeout or network issues.

### Solution:
- Implemented retry mechanism (3 attempts)
- If all retries fail → escalate to human

---

## 2. Invalid Order ID

### Problem:
Order ID not found in system.

### Solution:
- Executor detects missing data
- Stops further steps
- Escalates with proper message

---

## 3. Refund Not Eligible

### Problem:
User requests refund for non-refundable item.

### Solution:
- Eligibility check before refund
- If not eligible → escalate or reply accordingly

---

## 4. LLM Failure (Gemini API Issues)

### Problem:
- API key missing
- Model not available
- Response parsing error

### Solution:
- LLM is optional
- Fallback rule-based planner ensures continuity

---

## 5. Async Execution Errors

### Problem:
Improper async handling caused runtime crashes.

### Solution:
- Converted system to proper async/await model
- Removed nested event loops

---

## 🎯 Conclusion

System is designed to:
- Fail gracefully
- Avoid crashes
- Maintain service continuity