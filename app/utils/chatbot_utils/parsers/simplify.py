from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class SimplifyResponse(BaseModel):
    """
    Response model for simplifying an electrical circuit diagram.
    
    Attributes:
        description (str): A concise description of the electrical circuit diagram.
    """
    description: str = Field(..., description="A concise description of the electrical circuit diagram.")

simplify_parser = PydanticOutputParser(pydantic_object=SimplifyResponse)