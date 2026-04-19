
import streamlit as st
import json
import asyncio
import pandas as pd
import time

from agent.agent import process_ticket
from utils.metrics import METRICS

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AutoResolve AI", layout="wide", page_icon="🤖")

st.title("🤖 AutoResolve AI")
st.caption("Autonomous Support Resolution Agent")

# ---------------- STYLES ----------------
st.markdown("""
<style>
    .stMetric { text-align: center; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Controls")

mode = st.sidebar.selectbox(
    "Processing Mode",
    ["Batch Processing", "Single Ticket"]
)

show_logs = st.sidebar.checkbox("Show Execution Logs", value=False)

# ---------------- HELPER FUNCTIONS ----------------

def simulate_steps(steps):
    step_map = {
        "get_order": "🔍 Fetching order details...",
        "check_refund": "💰 Checking refund eligibility...",
        "issue_refund": "💸 Processing refund...",
        "search_kb": "📚 Searching knowledge base...",
        "send_reply": "✉️ Generating response..."
    }

    status = st.empty()

    for step in steps:
        status.info(step_map.get(step, f"⚙️ Executing {step}"))
        time.sleep(0.6)

    status.success("✅ Completed")


def type_writer(text):
    placeholder = st.empty()
    typed = ""

    for char in text:
        typed += char
        placeholder.markdown(f"📨 **Reply:** {typed}")
        time.sleep(0.01)


def render_ticket(ticket, result, show_logs=False):
    with st.expander(f"🧾 Ticket {ticket.get('ticket_id', 'N/A')}", expanded=True):

        col1, col2 = st.columns([3, 1])

        col1.markdown(f"**💬 Message:** {ticket.get('message', '')}")

        if result["decision"] == "resolved":
            col2.success("Resolved ✅")
        else:
            col2.error("Escalated ⚠️")

        st.write(f"🔺 Priority: **{result['priority']}**")

        # 🧠 Thinking animation
        st.info("🤖 Agent is thinking...")
        simulate_steps(result["results"].get("steps_executed", []))

        # 💬 Typing reply
        type_writer(result["results"].get("reply", ""))

        # 🧠 Reflection
        st.info(f"🧠 {result.get('reflection', '')}")

        # 🧩 Steps
        st.write("🧩 Steps:", result["results"].get("steps_executed"))

        # 🔍 Logs
        if show_logs:
            st.json(result["results"])

        st.divider()


# ---------------- SINGLE MODE ----------------

if mode == "Single Ticket":
    st.subheader("🧾 Single Ticket Processing")

    user_input = st.text_area("💬 Enter customer message")
    order_id = st.text_input("📦 Order ID")

    if st.button("🚀 Process Ticket"):
        if not user_input:
            st.warning("Please enter a message")
        else:
            ticket = {
                "ticket_id": 1,
                "message": user_input,
                "order_id": order_id
            }

            with st.spinner("Processing..."):
                result = asyncio.run(process_ticket(ticket))

            render_ticket(ticket, result, show_logs)


# ---------------- BATCH MODE ----------------

uploaded_file = st.file_uploader("📂 Upload Tickets JSON", type="json")

if uploaded_file and mode == "Batch Processing":

    tickets = json.load(uploaded_file)

    if st.button("🚀 Process All Tickets"):

        progress_bar = st.progress(0)
        results = []

        for i, ticket in enumerate(tickets):

            with st.spinner(f"Processing Ticket {i+1}..."):
                result = asyncio.run(process_ticket(ticket))

            results.append(result)

            render_ticket(ticket, result, show_logs)

            progress_bar.progress((i + 1) / len(tickets))

        # ---------------- ANALYTICS ----------------
        st.subheader("📊 Analytics Dashboard")

        df = pd.DataFrame(results)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Tickets", METRICS["total"])
        col2.metric("Success", METRICS["success"])
        col3.metric("Errors", METRICS["errors"])

        st.line_chart(df["confidence"])
        st.bar_chart(df["decision"].value_counts())
