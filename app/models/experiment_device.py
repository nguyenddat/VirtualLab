from sqlalchemy import *
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Experiment_Device(BareBaseModel):
    experiment_id = Column(Integer, ForeignKey("experiment.id"), nullable=False)
    device_id = Column(Integer, ForeignKey("device.id"), nullable=False)
    device_name = Column(String)
    properties = Column(JSONB)

    device = relationship("Device", back_populates="experiment_device")
    vertex = relationship("Vertex", back_populates="experiment_device")
    experiment = relationship("Experiment", back_populates="experiment_device")