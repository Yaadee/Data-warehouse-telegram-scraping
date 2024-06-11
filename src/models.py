from sqlalchemy import Column, Integer, Float
from .database import Base

class DetectionResult(Base):
    __tablename__ = 'detection_results'
    id = Column(Integer, primary_key=True, index=True)
    xmin = Column(Float)
    ymin = Column(Float)
    xmax = Column(Float)
    ymax = Column(Float)
    confidence = Column(Float)
    class_id = Column(Integer)
