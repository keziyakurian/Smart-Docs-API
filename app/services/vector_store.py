import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from app.core.config import settings

# Initialize Embeddings
# Note: This requires OPENAI_API_KEY to be set in .env
embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

# Initialize ChromaDB
# Persist to /tmp so it works on Vercel (Ephemeral)
PERSIST_DIRECTORY = "/tmp/chroma_db"

def get_vector_store():
    vector_store = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )
    return vector_store

def add_documents_to_store(chunks):
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    vector_store.persist()

def query_vector_store(query: str, k: int = 4):
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query, k=k)
    return results
