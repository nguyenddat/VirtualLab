from pydantic import BaseModel, Field

from app.models.basic_physics.base_device import BasePhysicsDevice


class BulbProperties(BaseModel):
    """
    Represents properties of a bulb in a basic physics simulation.
    """
    on: bool = Field(..., description="If the bulb is on")
    min_voltage: float = Field(..., description="Minimum voltage required for the bulb to turn on")
    max_voltage: float = Field(..., description="Maximum voltage the bulb can handle")
    left_socket_connected: bool = Field(..., description="If the left socket is connected")
    right_socket_connected: bool = Field(..., description="If the right socket is connected")


class Bulb(BasePhysicsDevice):
    """
    Represents a bulb in a basic physics simulation.
    """
    properties: BulbProperties = Field(..., description="The properties of the bulb")
    

