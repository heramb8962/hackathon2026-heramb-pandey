# 🤖 AutoResolve AI — Autonomous Support Resolution Agent

An intelligent, production-ready **Agentic AI system** that autonomously resolves customer support tickets using multi-step reasoning, tool orchestration, and real-time execution.

---

## 🚀 Problem Statement

E-commerce platforms handle thousands of repetitive support queries daily:

* Refund requests
* Order tracking
* Damaged products

Most of these are **predictable and automatable**, yet still handled manually—leading to delays, inconsistency, and high operational cost.

---

## 💡 Solution

AutoResolve AI is an **autonomous AI agent** that:

* Understands user intent
* Plans multi-step actions
* Executes backend tools
* Resolves queries end-to-end

> ⚡ Not just responding — **taking actions automatically**

---

## 🧠 Core Capabilities

### 🔁 Multi-Step Reasoning (Agentic Planning)

The agent converts queries into structured workflows:

```id="c5xwqk"
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
* Handles multiple tickets concurrently
* Scalable and production-ready

---

### 🔄 Retry & Failure Handling

* Automatic retries on failures
* Graceful degradation
* Prevents system crashes

---

### 🤖 Hybrid AI Planning

* LLM-based planning via **OpenRouter API (optional)**
* Rule-based fallback (zero-cost mode)
* Ensures reliability + flexibility

---

### 🧠 Intelligent Response Generation

* Context-aware replies
* Handles refund, tracking, KB, and edge cases
* Prevents incorrect responses

---

### 🧠 Memory System

* Stores past resolutions
* Reuses similar solutions
* Simulates real-world learning

---

### 🚨 Anomaly Detection

* Detects unclear or invalid inputs
* Prevents incorrect execution
* Escalates when necessary

---

### 📦 Order Validation System

* Validates order IDs
* Handles invalid/missing orders gracefully
* Prevents incorrect operations

---

### 🎯 Decision Engine

Each ticket produces:

* `resolved` / `escalated`
* confidence score

---

### 🧠 Self-Reflection (Explainability)

Example:

```id="4d8n2t"
"Agent successfully processed refund after validating eligibility."
```

---

### 📊 Audit Logging (VERY IMPORTANT)

* Logs every ticket execution
* Stores:

  * steps executed
  * tool calls
  * decisions
  * outputs
* Saved in: `audit_log.json`
* Covers all processed tickets

---

### 🎬 Real-Time Streaming UI

* Step-by-step execution visualization
* AI “thinking” simulation
* Typing-style responses

---

## 🔄 Processing Modes

### 🧾 Single Ticket Processing

* Real-time interaction
* Ideal for live demos

### 📂 Batch Processing

* Process multiple tickets
* Generates analytics
* Demonstrates scalability

---

## 🏗️ Architecture

Refer: `architecture.png`

```id="0m9xxt"
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
* Tool/service failure

---

## 📂 Project Structure

```id="0pl7l8"
agent/
tools/
services/
utils/
data/

demo/
  └── demo.mp4

architecture.png
failure_modes.md
audit_log.json
README.md

app.py
main.py
api.py
```

---

## 🛠️ Setup

### 1️⃣ Clone

```bash id="qk8i1y"
git clone https://github.com/heramb8962/hackathon2026-heramb-pandey
cd hackathon2026-heramb-pandey
```

---

### 2️⃣ Install Dependencies

```bash id="3q9r8t"
pip install -r requirements.txt
```

---

### 3️⃣ (Optional) Add API Key

```id="5wv0fa"
OPENROUTER_API_KEY=your_api_key_here
```

> ⚠️ System works even without API (fallback enabled)

---

## ▶️ Run

### CLI

```bash id="3sl3xn"
python main.py
```

---

### Streamlit UI

```bash id="ffk6mp"
streamlit run app.py
```

---

### FastAPI

```bash id="hz9k7o"
uvicorn api:app --reload
```

---

## 🎬 Demo Video

Watch here:

```id="4z2r1b"
demo/demo.mp4
```

---

## 🧪 Sample Execution

```id="h3d7sn"
Input: "My product is damaged"

→ Plan generated  
→ Order fetched  
→ Refund validated  
→ Refund processed  

Output: resolved (confidence: 0.95)
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
| Audit logging        | ✅      |
| Explainability       | ✅      |
| UI / UX              | ✅      |
| Production readiness | ✅      |

---

## 🎯 Future Scope

* Real API integrations
* Vector DB (RAG)
* Reinforcement learning loop
* Monitoring dashboards
* Multi-agent systems

---

## 👨‍💻 Author

**Heramb Pandey**
B.Tech CSE | AI Systems Enthusiast

---

## Live:
https://hackathon2026-heramb-pandey.onrender.com/

---

## 🏆 Final Note

> This is not just a chatbot.
> This is a **real-world autonomous AI agent capable of executing tasks end-to-end**.
