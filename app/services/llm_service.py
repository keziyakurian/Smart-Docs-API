from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from app.core.config import settings
from app.services.vector_store import get_vector_store

def get_llm():
    return ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY
    )

def get_qa_chain():
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    llm = get_llm()
    
    # Return source documents so we can see where the answer came from
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def answer_question(question: str):
    qa_chain = get_qa_chain()
    result = qa_chain.invoke({"query": question})
    return {
        "answer": result["result"],
        "source_documents": [doc.page_content for doc in result["source_documents"]]
    }
