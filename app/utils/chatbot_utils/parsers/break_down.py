from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class BreakDownResponse(BaseModel):
    """
    Response model for breaking down a question into smaller sub-questions.
    
    Attributes:
        subquestions (list[str]): List of sub-questions derived from the main question.
    """
    subquestions: list[str] = Field(..., description="List of sub-questions derived from the main question.")

break_down_parser = PydanticOutputParser(pydantic_object=BreakDownResponse)