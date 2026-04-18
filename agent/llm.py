import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

def get_plan(message):
    prompt = f"""
You are an intelligent AI support agent.

Available tools:
- get_order
- check_refund
- issue_refund
- send_reply

Rules:
- Use multiple steps for complex queries
- Always validate before action
- Return ONLY Python list

Ticket:
"{message}"
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",  # ✅ FIXED MODEL
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return '["get_order", "send_reply"]'