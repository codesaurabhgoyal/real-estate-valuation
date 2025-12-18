# Smart Property Advisor – Hessen 🇩🇪

This is an AI agent that helps with real estate queries using LangChain, LangGraph, FAISS, OpenAI, and Streamlit.

## How to Deploy

1. Upload this repo to GitHub.
2. Connect GitHub to Render.
3. Use the following build and start commands:

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn app.main:app --host=0.0.0.0 --port=8000 & streamlit run app/ui.py --server.port 8501 --server.enableCORS false
```

4. Add environment variable: `OPENAI_API_KEY`

Visit your app's public URL to use the property advisor.


## Author

**Saurabh Goyal**  
Senior Product & AI Consultant | Data, Cloud, AI Systems  
📍 Germany / Europe (Remote)

- LinkedIn: https://www.linkedin.com/in/saurabh-product-tech-strategy/
- GitHub: https://github.com/codesaurabhgoyal

