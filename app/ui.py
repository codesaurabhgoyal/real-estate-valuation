import streamlit as st
import requests
import os

st.title("🏡 Smart Property Advisor – Hessen 🇩🇪")

API_URL = os.getenv("API_URL", "http://localhost:8000")
query = st.text_area("🔍 Ask any property-related question")

if st.button("Ask AI"):
    if not query.strip():
        st.warning("Please enter your question.")
    else:
        try:
            with st.spinner("Thinking..."):
                res = requests.post(f"{API_URL}/ask", json={"prompt": query})
                
                if res.status_code == 200:
                    try:
                        answer = res.json().get("answer", "No answer returned.")
                        st.success(answer)
                    except Exception as json_err:
                        st.error("Received invalid JSON from backend.")
                else:
                    st.error(f"Error from backend: {res.status_code} - {res.text}")
        except Exception as e:
            st.error(f"Could not connect to backend: {e}")
