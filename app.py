import streamlit as st
import json
from agent.agent import process_ticket

st.title("🤖 AutoResolve AI - Support Agent")

uploaded_file = st.file_uploader("Upload tickets JSON", type="json")

if uploaded_file:
    tickets = json.load(uploaded_file)

    st.write("### Processing Tickets...")

    results = []

    for ticket in tickets:
        st.write(f"Processing Ticket {ticket['ticket_id']}...")
        result = process_ticket(ticket)
        results.append(result)

        st.success(f"Decision: {result['decision']} (confidence: {result['confidence']})")

    st.write("### Final Results")
    st.json(results)