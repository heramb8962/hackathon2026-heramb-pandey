import streamlit as st
import json
import pandas as pd
import asyncio
from agent.agent import process_ticket

st.set_page_config(page_title="AutoResolve AI", layout="wide")

st.title("🤖 AutoResolve AI - Intelligent Support Agent")

uploaded_file = st.file_uploader("Upload tickets JSON", type="json")

if uploaded_file:
    tickets = json.load(uploaded_file)

    if st.button("▶️ Process Tickets"):
        results = []

        for idx, ticket in enumerate(tickets):
            ticket_id = ticket.get("ticket_id", idx + 1)

            st.markdown(f"### 🧾 Ticket {ticket_id}")
            st.write(f"Message: {ticket.get('message', '')}")

            # ✅ FIX: run async properly
            result = asyncio.run(process_ticket(ticket))

            results.append(result)

            # Decision UI
            if result["decision"] == "resolved":
                st.success(f"✅ Resolved ({result['confidence']})")
            else:
                st.error(f"⚠️ Escalated ({result['confidence']})")

            st.write(f"🔺 Priority: {result['priority']}")

            st.json(result["results"])

        # 📊 Analytics
        st.subheader("📊 Analytics Dashboard")
        df = pd.DataFrame(results)
        st.bar_chart(df["confidence"])