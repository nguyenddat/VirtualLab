from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Import service thực tế
from services.rag_service import rag_service

load_dotenv()

router = APIRouter()

class TextbookQuery(BaseModel):
    subject: str  # Toán, Lý, Hóa, Sinh, Văn, Sử, Địa, etc.
    grade: str    # Lớp 6, 7, 8, 9, 10, 11, 12
    topic: str    # Chủ đề học sinh muốn tìm hiểu
    question: str # Câu hỏi cụ thể

class TextbookResponse(BaseModel):
    answer: str
    citations: List[dict]  # [{"page": 45, "content": "...", "chapter": "Chương 2"}]
    related_topics: List[str]
    confidence_score: float

class TextbookCitation(BaseModel):
    page: int
    content: str
    chapter: str
    section: Optional[str] = None

@router.post("/tutor/query", response_model=TextbookResponse)
async def ai_tutor_query(query: TextbookQuery):
    """
    AI gia sư với RAG từ sách giáo khoa
    Trả về câu trả lời với citation chính xác từ sách giáo khoa
    """
    try:
        # Sử dụng RAG service thực tế
        result = rag_service.generate_answer_with_citations(
            query=query.question,
            subject=query.subject,
            grade=query.grade
        )
        
        # Chuyển đổi citations từ RAG service sang format API
        citations = []
        for citation in result.get("citations", []):
            citations.append(TextbookCitation(
                page=citation.get("page", 1),
                content=citation.get("content", ""),
                chapter=citation.get("chapter", ""),
                section=citation.get("section")
            ))
        
        return TextbookResponse(
            answer=result.get("answer", "Không tìm thấy thông tin liên quan."),
            citations=citations,
            related_topics=[],  # TODO: Implement related topics extraction
            confidence_score=result.get("confidence_score", 0.0)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý câu hỏi: {str(e)}")

@router.get("/tutor/subjects")
async def get_available_subjects():
    """Lấy danh sách các môn học có sẵn"""
    return {
        "subjects": [
            {"id": "math", "name": "Toán học", "grades": ["6", "7", "8", "9", "10", "11", "12"]},
            {"id": "physics", "name": "Vật lý", "grades": ["6", "7", "8", "9", "10", "11", "12"]},
            {"id": "chemistry", "name": "Hóa học", "grades": ["8", "9", "10", "11", "12"]},
            {"id": "biology", "name": "Sinh học", "grades": ["6", "7", "8", "9", "10", "11", "12"]},
            {"id": "literature", "name": "Ngữ văn", "grades": ["6", "7", "8", "9", "10", "11", "12"]},
            {"id": "history", "name": "Lịch sử", "grades": ["6", "7", "8", "9", "10", "11", "12"]},
            {"id": "geography", "name": "Địa lý", "grades": ["6", "7", "8", "9", "10", "11", "12"]}
        ]
    } 