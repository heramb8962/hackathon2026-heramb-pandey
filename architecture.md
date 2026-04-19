# 🧠 Architecture Diagram – Autonomous Support Agent

## 🔄 System Flow

---

## 🧩 Components

### 1. Planner
- Generates multi-step plan
- Uses:
  - Rule-based logic
  - Optional Gemini LLM

---

### 2. Executor
- Executes steps asynchronously
- Handles retries and failures
- Tracks execution steps

---

### 3. Tools Layer
- `get_order`
- `check_refund`
- `issue_refund`
- `search_kb`

---

### 4. Decision Engine
- Determines:
  - resolved / escalated
- Assigns confidence score

---

### 5. Memory System
- Stores previous tickets
- Reuses past solutions

---

### 6. Metrics System
- Tracks:
  - latency
  - success rate
  - failures

---

### 7. Interfaces
- CLI (`main.py`)
- UI (`Streamlit`)
- API (`FastAPI`)

---

## ⚡ Key Features

- Async execution (concurrent tickets)
- Retry mechanism
- Hybrid AI (LLM + deterministic fallback)
- Production-ready modular design