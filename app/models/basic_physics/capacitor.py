from pydantic import BaseModel, Field

from app.models.basic_physics.base_device import BasePhysicsDevice

class CapacitorProperties(BaseModel):
    """Properties of a capacitor."""
    charged: bool = Field(..., description="Indicates if the capacitor is charged")
    capacitance: float = Field(..., description="Capacitance of the capacitor in farads")
    left_socket_connected: bool = Field(..., description="Indicates if the left socket is connected")
    right_socket_connected: bool = Field(..., description="Indicates if the right socket is connected")


class Capacitor(BasePhysicsDevice):
    """Represents a capacitor in a basic physics simulation."""
    properties: CapacitorProperties = Field(..., description="The properties of the capacitor")
