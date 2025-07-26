from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class SummaryResponse(BaseModel):
    response: str = Field(..., description = "Câu trả lời cuối cùng của bạn")


summary_parser = PydanticOutputParser(pydantic_object=SummaryResponse)