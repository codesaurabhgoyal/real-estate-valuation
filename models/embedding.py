from langchain.embeddings import OpenAIEmbeddings
from utils.config import settings

def get_embedding_model():
    return OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)