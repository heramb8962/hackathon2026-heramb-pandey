# hackathon2026-heramb-pandey
# AutoResolve AI 🚀

An Autonomous Support Resolution Agent built for KSolves Agentic AI Hackathon 2026

## 🔍 Problem

Customer support systems are overloaded with repetitive tickets. Most require multi-step reasoning and tool usage but are handled manually.

## 💡 Solution

AutoResolve AI is an agentic system that:

* Understands tickets
* Plans multi-step actions
* Uses tools (order lookup, refund, etc.)
* Handles failures intelligently
* Escalates when uncertain

## ⚙️ Features

* Multi-step reasoning agent
* Tool chaining (3+ calls per ticket)
* Retry + failure handling
* Concurrent ticket processing
* Confidence-based escalation
* Full audit logging

## 🏗️ Architecture

(attach your architecture.png later)

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```

## 📊 Demo

Processes 20 mock tickets end-to-end with logging

## 🧪 Failure Handling

* API timeout → retry
* Invalid data → fallback
* Low confidence → escalation

## 📁 Project Structure

(agent/, tools/, utils/, etc.)

## 👨‍💻 Author

Heramb Pandey
