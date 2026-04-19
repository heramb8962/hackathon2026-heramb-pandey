# 🤖 Autonomous Support Resolution Agent

An intelligent, production-ready AI agent designed to autonomously resolve customer support tickets using multi-step reasoning, tool orchestration, and hybrid AI planning.

---

## 🚀 Problem Statement

Modern e-commerce platforms receive hundreds of repetitive support tickets daily—refunds, order tracking, damaged items, etc. Most of these can be resolved automatically, yet they are still handled manually.

This project builds an **Agentic AI system** that:

* Understands customer issues
* Plans a sequence of actions
* Executes tools
* Resolves tickets autonomously

---

## 🧠 Key Features

### 🔁 Multi-Step Reasoning (Agentic Behavior)

The system does NOT respond in one step. It thinks in workflows:

```
get_order → check_refund → issue_refund → send_reply
```

---

### ⚙️ Tool-Based Execution

Implements real-world service simulation:

* `get_order(order_id)` → Fetch order details
* `check_refund_eligibility(order_id)` → Validate refund
* `issue_refund(order_id, amount)` → Process refund
* `search_knowledge_base(query)` → Answer FAQs
* `send_reply(ticket_id, message)` → Respond to user

---

### ⚡ Concurrent Processing

* Handles multiple tickets simultaneously
* Built using `asyncio`
* Improves scalability and performance

---

### 🔄 Retry & Failure Handling

* Automatic retry on tool failures
* Handles timeouts gracefully
* Ensures system does NOT crash

---

### 🤖 Hybrid AI Architecture

* Uses Gemini (optional) for intelligent planning
* Falls back to rule-based logic if API fails
* Ensures **zero-cost + reliability**

---

### 📊 Decision Engine

Each ticket produces:

* Final decision → `resolved` / `escalated`
* Confidence score

---

### 🧾 Audit Logging (Explainability)

* Logs every step of execution
* Stored in `audit_log.json`
* Tracks:

  * tool calls
  * decisions
  * outputs

---

### 🌐 Multiple Interfaces

| Interface | Description         |
| --------- | ------------------- |
| CLI       | Run using `main.py` |
| UI        | Streamlit dashboard |
| API       | FastAPI backend     |

---

## 🏗️ Architecture Overview

Refer to: `architecture.md`

### Flow:

```
Ticket Input
     ↓
Planner (LLM + Rule-based)
     ↓
Executor (Async Engine)
     ↓
Tools Layer (Order / Refund / KB)
     ↓
Decision Engine
     ↓
Response / Escalation
```

---

## ⚠️ Failure Handling

Refer to: `failure_modes.md`

Handled scenarios:

* API timeouts
* Invalid order IDs
* Refund rejection
* LLM failure
* Async execution errors

---

## 📂 Project Structure

```
agent/        → planner, executor, memory, decision logic
tools/        → simulated APIs (order, refund, product)
utils/        → retry, logging
services/     → knowledge base, metrics (optional)
models/       → schemas (optional)
data/         → sample tickets

main.py       → CLI runner
app.py        → Streamlit UI
api.py        → FastAPI server

architecture.md
failure_modes.md
audit_log.json
README.md
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/heramb8962/hackathon2026-heramb-pandey
cd hackathon2026-heramb-pandey
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ (Optional) Add Gemini API Key

Create a `.env` file in root:

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ If not provided, system uses fallback logic

---

## ▶️ Run the Project

### CLI Mode

```bash
python main.py
```

---

### Streamlit UI

```bash
streamlit run app.py
```

---

### FastAPI Server

```bash
uvicorn api:app --reload
```

---

## 🧪 Sample Execution

```
[AGENT] Processing ticket 1
[PLANNER] Final Plan: ['get_order', 'check_refund', 'issue_refund', 'send_reply']
[EXECUTOR] Executing plan...

Decision: resolved (confidence: 0.9)
```

---

## 📊 Evaluation Criteria Coverage

| Requirement                | Status |
| -------------------------- | ------ |
| Multi-step agent           | ✅      |
| Tool chaining              | ✅      |
| Concurrency                | ✅      |
| Failure handling           | ✅      |
| Audit logging              | ✅      |
| Explainability             | ✅      |
| Production-ready structure | ✅      |

---

## 🎯 Future Improvements

* Real database integration
* Advanced LLM reasoning
* Reinforcement learning loop
* Monitoring dashboard (Grafana)
* Real-time API integrations

---

## 👨‍💻 Author

**Heramb Pandey**
B.Tech CSE | AI & Systems Enthusiast

---

## 🏆 Final Note

> This is not just a chatbot.
> This is an autonomous agent designed for real-world deployment.
