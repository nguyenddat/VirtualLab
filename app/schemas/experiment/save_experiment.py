from typing import List, Set, Any, Dict, Optional

from pydantic import BaseModel

class Device(BaseModel):
    name: str
    type: str
    properties: Dict[str, Any]

class SaveExperimentRequest(BaseModel):
    chapter_id: int
    devices: List[Device]
    connections: List[Set[Any]]