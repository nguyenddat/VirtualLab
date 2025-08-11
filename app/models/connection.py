from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.base_class import BareBaseModel

class Connection(BareBaseModel):
    vertex_1_id = Column(Integer, ForeignKey("vertex.id"), nullable=False)
    vertex_2_id = Column(Integer, ForeignKey("vertex.id"), nullable=False)

    vertex_1 = relationship("Vertex", foreign_keys=[vertex_1_id])
    vertex_2 = relationship("Vertex", foreign_keys=[vertex_2_id])