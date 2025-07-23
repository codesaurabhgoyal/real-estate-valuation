import streamlit as st
import requests
import os

st.set_page_config(page_title="🏡 Smart Property Advisor", layout="centered")
st.title("🏡 Smart Property Advisor – Hessen 🇩🇪")

API_URL = os.getenv("API_URL", "http://localhost:8000")
query = st.text_area("🔍 Ask a property-related question")

if st.button("Ask AI"):
    if not query.strip():
        st.warning("Please enter your question.")
    else:
        try:
            with st.spinner("Thinking..."):
                res = requests.post(f"{API_URL}/ask", json={"prompt": query})
                if res.status_code == 200:
                    try:
                        st.success(res.json().get("answer", "✅ Done, but no answer."))
                    except Exception:
                        st.error("Invalid JSON returned from backend.")
                else:
                    st.error(f"Backend error: {res.status_code} - {res.text}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
