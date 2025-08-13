from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Vertex(BareBaseModel):
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    type = Column(String, nullable=False)

    experiment_device_id = Column(Integer, ForeignKey("experiment_device.id"), nullable=False)

    connections_as_vertex_1 = relationship("Connection", foreign_keys="Connection.vertex_1_id", back_populates="vertex_1")
    connections_as_vertex_2 = relationship("Connection", foreign_keys="Connection.vertex_2_id", back_populates="vertex_2")