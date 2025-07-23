import streamlit as st
import requests
import os

st.title("🏡 Smart Property Advisor – Hessen 🇩🇪")
query = st.text_area("🔍 Enter your query")

if st.button("Ask AI"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        API_URL = os.getenv("API_URL", "http://localhost:8000")
        response = requests.post(f"{API_URL}/ask", json={"prompt": query})
        st.success(response.json()["answer"])
