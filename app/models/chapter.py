from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Chapter(BareBaseModel):
    name = Column(String, nullable=False)
    description = Column(String)

    bookset_id = Column(Integer, ForeignKey("bookset.id"), nullable=False)

    bookset = relationship("BookSet", back_populates="chapter")
    experiment = relationship("Experiment", back_populates="chapter")