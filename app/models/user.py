from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class User(BareBaseModel):
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

