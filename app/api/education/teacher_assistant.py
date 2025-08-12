from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Import service thực tế
from services.teacher_assistant_service import teacher_assistant_service

load_dotenv()

router = APIRouter()

class TeacherQuery(BaseModel):
    subject: str
    grade: str
    topic: str
    question: str
    context: Optional[str] = None  # Bối cảnh giảng dạy

class TeacherResponse(BaseModel):
    answer: str
    teaching_tips: List[str]
    common_mistakes: List[str]
    assessment_questions: List[str]
    resources: List[str]

@router.post("/teacher/assist", response_model=TeacherResponse)
async def ai_teacher_assistant(query: TeacherQuery):
    """
    AI hỗ trợ giáo viên - trả lời câu hỏi và đưa ra gợi ý giảng dạy
    """
    try:
        # Sử dụng service thực tế thay vì dữ liệu cố định
        result = teacher_assistant_service.generate_teaching_response(
            query=query.question,
            subject=query.subject,
            grade=query.grade,
            context=query.context,
            topic=query.topic
        )
        
        return TeacherResponse(**result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý câu hỏi: {str(e)}")

@router.post("/teacher/lesson-plan")
async def generate_lesson_plan(subject: str, grade: str, topic: str, duration: int = 45):
    """
    Tạo kế hoạch bài giảng
    """
    try:
        # Sử dụng service thực tế
        result = teacher_assistant_service.generate_lesson_plan(
            subject=subject,
            grade=grade,
            topic=topic,
            duration=duration
        )
        
        return {"lesson_plan": result}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi tạo kế hoạch bài giảng: {str(e)}")

@router.post("/teacher/assessment")
async def generate_assessment(subject: str, grade: str, topic: str, difficulty: str = "medium"):
    """
    Tạo bài kiểm tra/đánh giá
    """
    try:
        # Sử dụng service thực tế
        result = teacher_assistant_service.generate_assessment(
            subject=subject,
            grade=grade,
            topic=topic,
            difficulty=difficulty
        )
        
        return {"assessment": result}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi tạo bài kiểm tra: {str(e)}") 