import os
import requests
from dotenv import load_dotenv

load_dotenv()

def llm_plan(message):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        print("[LLM] No OpenRouter key found, using fallback")
        return None

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        prompt = f"""
You are an intelligent customer support AI agent planner.

Your job is to convert user messages into a sequence of actions.

Available actions:
- get_order
- check_refund
- issue_refund
- search_kb
- send_reply

Rules:
1. Always include 'get_order' before refund-related steps
2. Refund flow must be:
   get_order → check_refund → issue_refund
3. Use 'search_kb' for general questions
4. Always end with 'send_reply'
5. Return ONLY a Python list

Examples:

Message: "I want a refund for damaged product"
Output: ["get_order", "check_refund", "issue_refund", "send_reply"]

Message: "Where is my order?"
Output: ["get_order", "send_reply"]

Message: "How can I cancel my order?"
Output: ["search_kb", "send_reply"]

Now process:

Message: {message}
"""

        data = {
            "model": "openai/gpt-3.5-turbo",  # safe free model
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" not in result:
            print("[LLM ERROR]", result)
            return None

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return None