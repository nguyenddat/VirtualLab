from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv
import base64
import io
from PIL import Image

# Import service thực tế
from services.image_generator_service import image_generator_service

load_dotenv()

router = APIRouter()

class ToolGenerationRequest(BaseModel):
    description: str  # Mô tả dụng cụ cần tạo
    subject: str      # Môn học (Vật lý, Hóa học, Sinh học, etc.)
    grade: str        # Lớp học
    style: Optional[str] = "realistic"  # realistic, cartoon, technical
    size: Optional[str] = "medium"      # small, medium, large

class ToolGenerationResponse(BaseModel):
    image_url: str
    image_base64: str
    description: str
    usage_instructions: List[str]
    safety_notes: Optional[str] = None
    related_experiments: List[str]

@router.post("/tools/generate", response_model=ToolGenerationResponse)
async def generate_educational_tool(request: ToolGenerationRequest):
    """
    AI tạo sinh dụng cụ giáo dục từ mô tả văn bản
    """
    try:
        # Sử dụng ImageGeneratorService thực tế
        result = image_generator_service.generate_educational_tool_image(
            description=request.description,
            subject=request.subject,
            style=request.style
        )
        
        # Tạo hướng dẫn sử dụng
        usage_instructions = image_generator_service.generate_usage_instructions(
            description=request.description,
            subject=request.subject
        )
        
        # Tạo ghi chú an toàn
        safety_notes = image_generator_service.generate_safety_notes(
            description=request.description,
            subject=request.subject
        )
        
        return ToolGenerationResponse(
            image_url=result.get("image_url", ""),
            image_base64=result.get("image_base64", ""),
            description=f"Dụng cụ {request.description} cho môn {request.subject} lớp {request.grade}",
            usage_instructions=usage_instructions,
            safety_notes=safety_notes,
            related_experiments=[
                "Thí nghiệm 1: Khảo sát tính chất của dụng cụ",
                "Thí nghiệm 2: Đo lường các thông số cơ bản",
                "Thí nghiệm 3: Ứng dụng trong thực tế"
            ]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi tạo dụng cụ: {str(e)}")

@router.get("/tools/categories")
async def get_tool_categories():
    """
    Lấy danh sách các loại dụng cụ theo môn học
    """
    return {
        "categories": {
            "physics": {
                "name": "Vật lý",
                "tools": [
                    "Máy đo điện áp",
                    "Đồng hồ đo thời gian",
                    "Thước đo",
                    "Cân điện tử",
                    "Máy phát sóng",
                    "Máy đo nhiệt độ"
                ]
            },
            "chemistry": {
                "name": "Hóa học", 
                "tools": [
                    "Ống nghiệm",
                    "Bình cầu",
                    "Pipet",
                    "Cân phân tích",
                    "Máy đo pH",
                    "Bếp đun"
                ]
            },
            "biology": {
                "name": "Sinh học",
                "tools": [
                    "Kính hiển vi",
                    "Lame kính",
                    "Máy đo nhịp tim",
                    "Thiết bị đo huyết áp",
                    "Máy đo nhiệt độ cơ thể",
                    "Dụng cụ thí nghiệm ADN"
                ]
            },
            "mathematics": {
                "name": "Toán học",
                "tools": [
                    "Thước đo góc",
                    "Compa",
                    "Êke",
                    "Thước đo độ dài",
                    "Máy tính bỏ túi",
                    "Bộ hình học"
                ]
            }
        }
    }

@router.post("/tools/validate")
async def validate_tool_description(description: str, subject: str):
    """
    Kiểm tra tính hợp lệ của mô tả dụng cụ
    """
    try:
        # Sử dụng ImageGeneratorService để validate
        result = image_generator_service.validate_tool_description(
            description=description,
            subject=subject
        )
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi kiểm tra: {str(e)}")

@router.get("/tools/templates")
async def get_tool_templates(subject: str):
    """
    Lấy các template mô tả dụng cụ theo môn học
    """
    templates = {
        "physics": [
            "Máy đo điện áp 0-12V với màn hình LCD, dùng cho thí nghiệm mạch điện",
            "Đồng hồ bấm giây độ chính xác 0.01s, có chức năng đo thời gian phản ứng",
            "Thước đo độ dài 0-100cm với vạch chia mm, làm bằng thép không gỉ"
        ],
        "chemistry": [
            "Ống nghiệm thủy tinh 15ml với nút bịt, dùng cho thí nghiệm hóa học",
            "Bình cầu 250ml có cổ nhám, phù hợp cho thí nghiệm chưng cất",
            "Pipet 10ml có vạch chia 0.1ml, làm bằng thủy tinh borosilicate"
        ],
        "biology": [
            "Kính hiển vi quang học độ phóng đại 400x, có đèn LED tích hợp",
            "Lame kính 76x26mm với lam kính 1.0-1.2mm, dùng cho quan sát tế bào",
            "Máy đo nhịp tim cầm tay với cảm biến quang học, hiển thị số nhịp/phút"
        ]
    }
    
    return {
        "subject": subject,
        "templates": templates.get(subject, [])
    } 