from pydantic import BaseModel, Field

from models.basic_physics.base_device import BasePhysicsDevice

class AmmeterProperties(BaseModel):
    """
    Represents properties of an ammeter in a basic physics simulation.
    """
    current: float = Field(..., description="The current measured by the ammeter")
    left_socket_connected: bool = Field(..., description="If the left socket is connected")
    right_socket_connected: bool = Field(..., description="If the right socket is connected")


class Ammeter(BasePhysicsDevice):
    """
    Represents an ammeter in a basic physics simulation.
    """
    properties: AmmeterProperties = Field(..., description="The properties of the ammeter")