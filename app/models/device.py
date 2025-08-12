from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Device(BareBaseModel):
    type = Column(String, nullable=False)

    experiment_device = relationship("Experiment_Device", back_populates="device")