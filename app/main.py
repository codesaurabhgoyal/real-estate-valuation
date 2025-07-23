from fastapi import FastAPI
from pydantic import BaseModel
from app.chains import get_qa_chain
from models.llm import get_llm
from scripts.build_index import build_vector_store
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend → backend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your Streamlit URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str

# Load components
vector_store = build_vector_store()
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
llm = get_llm()
qa_chain = get_qa_chain(llm, retriever)

# /ask endpoint (used by frontend)
@app.post("/ask")
async def ask(query: Query):
    try:
        result = qa_chain.run(query.prompt)
        return {"answer": result}
    except Exception as e:
        return {"error": str(e)}
