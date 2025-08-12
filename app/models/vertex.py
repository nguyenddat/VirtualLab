from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Vertex(BareBaseModel):
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)

    experiment_device_id = Column(Integer, ForeignKey("experiment_device.id"), nullable=False)

    connection = relationship("Connection", back_populates="vertex")
    experiment_device = relationship("Experiment_Device", back_populates="vertex")