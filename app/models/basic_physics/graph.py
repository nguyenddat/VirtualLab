from typing import List, Set

from pydantic import BaseModel, Field

from models.basic_physics import ammeter, battery, capacitor, voltmeter, wire, bulb

class Device(BaseModel):
    """Represents a device in the electrical circuit."""
    name: str = Field(..., description="The name of the device")
    type: str = Field(..., description="The type of the device")
    properties: dict = Field(..., description="The properties of the device")


class ElecGraph(BaseModel):
    """Represents an electrical circuit graph."""
    devices: List[Device] = Field(..., description="List of devices in the electrical circuit except wires")
    connections: List[Set[str]] = Field(...,description="List of wires connecting the devices in the electrical circuit")
