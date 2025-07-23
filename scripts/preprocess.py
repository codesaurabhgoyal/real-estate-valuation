from langchain.text_splitter import RecursiveCharacterTextSplitter

def preprocess_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    processed = []
    for doc in documents:
        chunks = splitter.split_text(doc['page_content'])
        for chunk in chunks:
            processed.append({"page_content": chunk, "metadata": doc.get("metadata", {})})
    return processed