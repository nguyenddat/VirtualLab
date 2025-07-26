from pydantic import BaseModel, Field

from app.models.basic_physics.graph import ElecGraph

class ElecRequest(BaseModel):
    """Request model for electrical circuit operations."""
    graph: ElecGraph = Field(
        ...,
        description="The electrical circuit graph containing devices and connections"
    )

    question: str = Field(
        ...,
        description="Student's question"
    )