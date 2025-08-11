from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel

class DeviceResponse(BaseModel):
    name: str
    type: str
    properties: Dict[str, Any]

class ExperimentResponse(BaseModel):
    experiment_id: int
    name: str
    description: Optional[str]
    devices: List[DeviceResponse]
    connections: List[Dict[str, Any]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class ExperimentSummary(BaseModel):
    id: int
    name: str
    description: Optional[str]
    device_count: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class ExperimentsListResponse(BaseModel):
    experiments: List[ExperimentSummary]
    total: int
    skip: int
    limit: int

class SaveExperimentResponse(BaseModel):
    message: str
    experiment_id: int
    devices_count: int
    connections_count: int

class DeleteExperimentResponse(BaseModel):
    message: str
    experiment_id: int
