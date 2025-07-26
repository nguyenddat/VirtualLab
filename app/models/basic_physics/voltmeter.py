from pydantic import BaseModel, Field

from app.models.basic_physics.base_device import BasePhysicsDevice


class VoltmeterProperties(BaseModel):
    """Properties of a voltmeter."""
    current: float = Field(..., description="Current flowing through the voltmeter in amperes")
    left_socket_connected: bool = Field(..., description="Indicates if the left socket is connected")
    right_socket_connected: bool = Field(..., description="Indicates if the right socket is connected")


class Voltmeter(BasePhysicsDevice):
    """Represents a voltmeter in a basic physics simulation."""
    properties: VoltmeterProperties = Field(..., description="The properties of the voltmeter")