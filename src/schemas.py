
# from pydantic import BaseModel
# from datetime import datetime

# class DetectionResultBase(BaseModel):
#     image_id: str
#     x_min: float
#     y_min: float
#     x_max: float
#     y_max: float
#     confidence: float
#     class_id: int
#     class_name: str

# class DetectionResultCreate(DetectionResultBase):
#     pass

# class DetectionResult(DetectionResultBase):
#     id: int

#     class Config:
#         from_attributes = True 

from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_id: str
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    confidence: float
    class_id: int
    class_name: str
class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        from_attributes = True
