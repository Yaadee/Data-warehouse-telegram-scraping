# from pydantic import BaseModel
# from datetime import datetime

# class DetectionResultBase(BaseModel):
#     xmin: float
#     ymin: float
#     xmax: float
#     ymax: float
#     confidence: float
#     class_id: int

# class DetectionResultCreate(DetectionResultBase):
#     pass

# class DetectionResult(DetectionResultBase):
#     id: int
#     timestamp: datetime

#     class Config:
#         from_attributes = True


from pydantic import BaseModel
from datetime import datetime

class DetectionResultBase(BaseModel):
    image_id: str
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    confidence: float
    class_id: int
    class_name: str

class ItemCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True 

