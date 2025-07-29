from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class CreateToolResponse(BaseModel):
    image: str = Field(..., description="Image của bạn trả về dưới dạng base64")

create_tool_parser = PydanticOutputParser(pydantic_object=CreateToolResponse)
