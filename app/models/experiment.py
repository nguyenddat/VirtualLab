from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Experiment(BareBaseModel):
    name = Column(String, nullable=False)
    description = Column(String)

    status = Column(String, nullable=False, default="blank")
    public_status = Column(String, nullable=False, default="private")
    
    chapter_id = Column(Integer, ForeignKey("chapter.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)

    chapter = relationship("Chapter", back_populates="experiment")
    experiment_device = relationship("Experiment_Device", back_populates="experiment")