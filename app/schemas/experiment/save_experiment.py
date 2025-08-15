from typing import List, Set, Any, Dict, Optional

from pydantic import BaseModel

class CreateExperimentRequest(BaseModel):
    name: str
    status: str
    public_status: str
    description: Optional[str] = None
    
    chapter_id: int

class CreateExperimentDeviceRequest(BaseModel):
    experiment_id: int
    devices: List[Any]
    connections: List[Any]

class UpdateExperimentRequest(BaseModel):
    experiment_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    public_status: Optional[str] = None
    chapter_id: Optional[int] = None