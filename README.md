# 🤖 AutoResolve AI — Autonomous Support Resolution Agent

An intelligent, production-ready **Agentic AI system** that autonomously resolves customer support tickets using multi-step reasoning, tool orchestration, and real-time execution.

---

## 🚀 Problem Statement

E-commerce platforms handle thousands of repetitive support queries daily:

* Refund requests
* Order tracking
* Damaged products

Most of these are **rule-based and automatable**, yet still handled manually.

---

## 💡 Solution

AutoResolve AI is an **autonomous support agent** that:

* Understands user intent
* Plans actions dynamically
* Executes backend tools
* Resolves issues end-to-end

> ⚡ This is not a chatbot — it is an **action-oriented AI agent**

---

## 🧠 Core Capabilities

### 🔁 Multi-Step Reasoning (Agentic Planning)

The agent converts user queries into structured workflows:

```
get_order → check_refund → issue_refund → send_reply
```

---

### ⚙️ Tool-Orchestrated Execution

Simulated real-world services:

* `get_order(order_id)` → Fetch order details
* `check_refund_eligibility(order)` → Validate refund
* `issue_refund(order_id, amount)` → Process refund
* `search_kb(query)` → Answer FAQs
* `send_reply()` → Generate response

---

### ⚡ Async Execution Engine

* Built using `asyncio`
* Handles multiple tickets efficiently
* Scalable and production-aligned

---

### 🔄 Retry & Failure Handling

* Automatic retries on failures
* Graceful degradation
* No system crashes

---

### 🤖 Hybrid AI Planning

* LLM-based planning using **OpenRouter API (optional)**
* Rule-based fallback (zero-cost mode)
* Ensures reliability + flexibility

---

### 🧠 Intelligent Response Generation

* Context-aware replies
* Dynamic based on execution results
* Handles edge cases gracefully

---

### 🧠 Memory System

* Stores previous resolutions
* Reuses past solutions for efficiency
* Simulates real-world agent learning

---

### 🎯 Decision Engine

Each ticket produces:

* `resolved` / `escalated`
* confidence score

---

### 🧠 Self-Reflection (Explainability)

Agent explains its own behavior:

```
"Agent successfully processed refund after validating eligibility."
```

---

### 🎬 Real-Time Streaming UI

* Step-by-step execution visualization
* AI “thinking” simulation
* Typing effect responses

---

## 🔄 Processing Modes

AutoResolve AI supports **both real-world usage scenarios**:

### 🧾 Single Ticket Processing

* Enter a single query manually
* Ideal for debugging and live demos

### 📂 Batch Processing

* Upload JSON file with multiple tickets
* Processes all tickets sequentially with analytics
* Demonstrates scalability

---

## 🏗️ Architecture

Refer: `architecture.md`

```
User Input
    ↓
Planner (LLM + Rule-based)
    ↓
Executor (Async Engine)
    ↓
Tools Layer
    ↓
Decision Engine
    ↓
Response Generator
```

---

## ⚠️ Failure Handling

Refer: `failure_modes.md`

Handled scenarios:

* API timeouts
* Invalid order IDs
* Refund rejection
* LLM failure
* Service outages

---

## 📂 Project Structure

```
agent/
  ├── planner.py
  ├── executor_async.py
  ├── memory.py
  ├── agent.py
  ├── response_generator.py

tools/
  ├── order.py
  ├── refund.py
  ├── product.py

services/
  ├── kb.py

utils/
  ├── retry.py
  ├── logger.py
  ├── metrics.py

data/
  ├── tickets.json

app.py        → Streamlit UI
main.py       → CLI runner
api.py        → FastAPI server

README.md
architecture.md
failure_modes.md
audit_log.json
```

---

## 🛠️ Setup

### 1️⃣ Clone

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

### 3️⃣ (Optional) Add OpenRouter API Key

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

> ⚠️ If not provided, system automatically falls back to rule-based planning

---

## ▶️ Run the Project

### 🖥 CLI Mode

```bash
python main.py
```

---

### 🌐 Streamlit UI

```bash
streamlit run app.py
```

---

### ⚡ FastAPI Server

```bash
uvicorn api:app --reload
```

---

## 🧪 Sample Execution

```
User: "My product is damaged, I want refund"

→ Plan generated  
→ Order fetched  
→ Refund validated  
→ Refund processed  
→ Response generated  

Decision: resolved (confidence: 0.95)
```

---

## 📊 Evaluation Coverage

| Criteria             | Status |
| -------------------- | ------ |
| Multi-step reasoning | ✅      |
| Tool orchestration   | ✅      |
| Async execution      | ✅      |
| Failure handling     | ✅      |
| Memory system        | ✅      |
| Explainability       | ✅      |
| UI / UX              | ✅      |
| Production readiness | ✅      |

---

## 🎯 Future Scope

* Real API integrations
* Vector database (RAG)
* Reinforcement learning loop
* Monitoring dashboard (Grafana)
* Multi-agent collaboration

---

## 👨‍💻 Author

**Heramb Pandey**
B.Tech CSE | AI Systems Enthusiast

---

## 🏆 Final Note

> This is not just a chatbot.
> This is an **autonomous AI agent capable of real-world task execution**.
