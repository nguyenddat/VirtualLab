from pydantic import BaseModel, Field

from app.models.basic_physics.base_device import BasePhysicsDevice

class BatteryProperties(BaseModel):
    """Properties of a battery."""
    voltage: float = Field(..., description="Voltage of the battery in volts")
    left_socket: str = Field(..., description="If left socket's polarity is positive, it is 'positive', otherwise 'negative'")
    right_socket: str = Field(..., description="If right socket's polarity is positive, it is 'positive', otherwise 'negative'")


class Battery(BasePhysicsDevice):
    """Represents a battery in a basic physics simulation."""
    properties: BatteryProperties = Field(..., description="The properties of the battery")