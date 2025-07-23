from langchain.llms import OpenAI
from utils.config import settings

def get_llm():
    return OpenAI(openai_api_key=settings.OPENAI_API_KEY, temperature=0)