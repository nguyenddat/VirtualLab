from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class BookSet(BareBaseModel):
    name = Column(String, nullable=False)
    description = Column(String)

    book = relationship("Book", back_populates="bookset")