from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from pydantic import BaseModel
from app.services.document_service import save_upload_file, process_pdf
from app.services.vector_store import add_documents_to_store
from app.services.llm_service import answer_question

router = APIRouter()

class QueryRequest(BaseModel):
    items: List[dict] # Placeholder, better to be specific but strict pydantic often fights with flexible json inputs in quick prototypes. 
    # Actually, let's make it simple:
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]

@router.get("/")
def read_root():
    return {"message": "Welcome to Smart Docs API"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # 1. Save file locally
    file_path = await save_upload_file(file)
    
    # 2. Process PDF (Extract text & Chunk)
    chunks = process_pdf(file_path)
    
    # 3. Add to Vector Store (Embedding & Indexing)
    add_documents_to_store(chunks)
    
    return {"filename": file.filename, "message": "File uploaded and processed successfully", "chunks_count": len(chunks)}

@router.post("/query", response_model=QueryResponse)
def query_document(request: QueryRequest):
    result = answer_question(request.question)
    return QueryResponse(answer=result["answer"], sources=result["source_documents"])

