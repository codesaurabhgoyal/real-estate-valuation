import os
from langchain.vectorstores import FAISS
from models.embedding import get_embedding_model
from scripts.raw_ingest import ingest
from scripts.preprocess import preprocess_documents

def build_vector_store(persist_path="faiss_index"):
    docs = preprocess_documents(ingest())
    embeddings = get_embedding_model()
    if os.path.exists(persist_path):
        vs = FAISS.load_local(persist_path, embeddings)
        vs.add_documents(docs)
    else:
        vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(persist_path)
    return vs