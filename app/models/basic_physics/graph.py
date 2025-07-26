from typing import List, Union

from pydantic import BaseModel, Field

from app.models.basic_physics import ammeter, battery, capacitor, voltmeter, wire, bulb


class ElecGraph(BaseModel):
    """Represents an electrical circuit graph."""
    devices: List[Union[
        ammeter.Ammeter,
        battery.Battery,
        capacitor.Capacitor,
        voltmeter.Voltmeter,
        bulb.Bulb
    ]] = Field(
        ...,
        description="List of devices in the electrical circuit except wires"
    )

    connections: List[wire.Wire] = Field(
        ...,
        description="List of wires connecting the devices in the electrical circuit"
    )
