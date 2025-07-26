from typing import List

from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class IntentClassifyResponse(BaseModel):
    """
    Response model for intent classification.
    
    Attributes:
        can_answer (bool): Indicates if the question can be answered directly.
        reasoning_needed (bool): Indicates if reasoning is needed to answer the question.
    """
    can_answer: bool = Field(..., description="True nếu câu trả lời có thể trả lời được ngay")
    subquestion: str = Field(..., description="Nếu chưa trả lời được ngay thì câu hỏi gì cần phân tích thêm")
    response: str = Field(..., description="Câu trả lời của bạn nếu có thể trả lời ngay")
    recommendations: List[str] = Field(..., description="Các hành động có thể áp dụng để giải quyết vấn đề")

intent_classify_parser = PydanticOutputParser(pydantic_object=IntentClassifyResponse)