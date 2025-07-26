from typing import List, Optional

from pydantic import BaseModel

class State(BaseModel):
    """
    Represents the state of the chatbot.
    """
    question: str

    graph: str
    data: List[str]

    response: Optional[str] = None
    recommendations: Optional[List[str]] = None