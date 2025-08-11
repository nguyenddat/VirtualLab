from typing import *

from pydantic import BaseModel, Field

# class Graph(BaseModel):
#     devices: List[Any] = Field(..., description="The devices in the circuit.")
#     connections: List[Set[Any]] = Field(..., description="The connections between the devices.")

class ElectricExplainRequest(BaseModel):
    graph: str
    question: str