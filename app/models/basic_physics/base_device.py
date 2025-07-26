from typing import Dict, Any

from pydantic import BaseModel, Field

class BasePhysicsDevice(BaseModel):
    """
    Represents a base class for devices in a basic physics simulation.
    """
    name: str = Field(..., description="The name of the device")
    type: str = Field(..., description="The type of the device")
    position: Dict[str, float] = Field(..., description="The position of the device in the simulation space")
    properties: Any = Field(..., description="The properties of the device")
    
    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True