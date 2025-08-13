from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Book(BareBaseModel):
    name = Column(String, nullable=False)
    grade = Column(Integer, nullable=False)

    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)
    bookset_id = Column(Integer, ForeignKey("bookset.id"), nullable=False)

    static_file_path = Column(String)
    
    chapter = relationship("Chapter", back_populates="book")
    subject = relationship("Subject", back_populates="book")
    bookset = relationship("BookSet", back_populates="book")