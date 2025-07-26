from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class IntentClassifyResponse(BaseModel):
    """
    Response model for intent classification.
    
    Attributes:
        can_answer (bool): Indicates if the question can be answered directly.
        reasoning_needed (bool): Indicates if reasoning is needed to answer the question.
    """
    can_answer: bool = Field(..., description="Indicates if the question can be answered directly.")
    subquestion: str = Field(..., description="Sub-question if reasoning is needed to answer the main question.")
    response: str = Field(..., description="The response to the question if it can be answered directly.")

intent_classify_parser = PydanticOutputParser(pydantic_object=IntentClassifyResponse)