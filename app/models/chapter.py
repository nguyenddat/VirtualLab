from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.base_class import BareBaseModel

class Chapter(BareBaseModel):
    name = Column(String, nullable=False)
    description = Column(String)

    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)

    book = relationship("Book", back_populates="chapter")
    experiment = relationship("Experiment", back_populates="chapter")