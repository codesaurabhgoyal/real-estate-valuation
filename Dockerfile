FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV OPENAI_API_KEY=your_openai_api_key
EXPOSE 8000
CMD ["bash", "-c", "uvicorn app.main:app --host=0.0.0.0 --port=8000 & streamlit run app/ui.py --server.port 8501 --server.enableCORS false"]