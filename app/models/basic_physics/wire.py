from pydantic import BaseModel, Field


class WireProperties(BaseModel):
    """Properties of a wire."""
    from_socket: str = Field(..., alias="from", description="A device's socket where the wire starts")
    to_socket: str = Field(..., alias="to", description="A device's socket where the wire ends")

    class Config:
        validate_by_name = True

        
class Wire(BaseModel):
    """Represents a wire in a basic physics simulation."""
    name: str = Field(..., description="Name of the wire")
    type: str = Field(..., description="Wire")
    properties: WireProperties = Field(..., description="The properties of the wire")


