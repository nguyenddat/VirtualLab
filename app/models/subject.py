from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.base_class import BareBaseModel

class Subject(BareBaseModel):
    name = Column(String, nullable=False)
    description = Column(String)

    book = relationship("Book", back_populates="subject")