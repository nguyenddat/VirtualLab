from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class ExtractToolResponse(BaseModel):
    response: str = Field(..., description="1 vật thể chính kèm mô tả của vật thể đó.")

extract_tool_parser = PydanticOutputParser(pydantic_object=ExtractToolResponse)