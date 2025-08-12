from typing import List
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Citation(BaseModel):
    summary: str = Field(..., description="Tóm tắt nội dung nguồn trích dẫn")
    page: int = Field(..., description="Số trang trong sách giáo khoa")
    filename: str = Field(..., description="Tên file sách giáo khoa")

class RagResponse(BaseModel):
    response: str = Field(..., description="Câu trả lời gồm 2 đoạn văn như yêu cầu")
    citations: List[Citation] = Field(..., description="Danh sách các nguồn trích dẫn")

rag_parser = PydanticOutputParser(pydantic_object=RagResponse)