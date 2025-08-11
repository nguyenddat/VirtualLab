from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.base_class import BareBaseModel

class BookSet(BareBaseModel):
    name = Column(String, nullable=False)
    description = Column(String)
    static_image_path = Column(String)
    static_file_path = Column(String)

    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)

    subject = relationship("Subject", back_populates="bookset")
    chapter = relationship("Chapter", back_populates="bookset")