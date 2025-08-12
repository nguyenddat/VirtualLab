from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.models.base_class import BareBaseModel

class Experiment(BareBaseModel):
    name = Column(String, nullable=False)
    content = Column(String)
    description = Column(String)
    static_image_path = Column(String)
    
    chapter_id = Column(Integer, ForeignKey("chapter.id"), nullable=False)

    chapter = relationship("Chapter", back_populates="experiment")
    experiment_device = relationship("Experiment_Device", back_populates="experiment")