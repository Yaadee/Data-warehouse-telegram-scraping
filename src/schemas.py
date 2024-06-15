# schemas.py

from pydantic import BaseModel
from datetime import datetime

class DetectionResultBase(BaseModel):
    image_id: str
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    class_id: int
    class_name: str
    timestamp: datetime

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True
















# # schemas.py

# from pydantic import BaseModel
# from typing import Optional

# class DetectionResultBase(BaseModel):
#     image_id: str
#     xmin: float
#     ymin: float
#     xmax: float
#     ymax: float
#     confidence: float
#     class_id: int
#     class_name: str

# class DetectionResultCreate(DetectionResultBase):
#     pass

# class DetectionResult(DetectionResultBase):
#     id: int
#     timestamp: Optional[str]

#     class Config:
#         orm_mode = True
