# from sqlalchemy import Column, Integer, Float, DateTime
# from database import Base
# from datetime import datetime

# class DetectionResult(Base):
#     __tablename__ = "detection_results"

#     id = Column(Integer, primary_key=True, index=True)
#     xmin = Column(Float, nullable=False)
#     ymin = Column(Float, nullable=False)
#     xmax = Column(Float, nullable=False)
#     ymax = Column(Float, nullable=False)
#     confidence = Column(Float, nullable=False)
#     class_id = Column(Integer, nullable=False)
#     timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)



from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class DetectionResult(Base):
    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(String)
    x_min = Column(Float)
    y_min = Column(Float)
    x_max = Column(Float)
    y_max = Column(Float)
    confidence = Column(Float)
    class_id = Column(Integer)
    class_name = Column(String)
    timestamp = Column(DateTime)
