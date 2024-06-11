from pydantic import BaseModel

class DetectionResult(BaseModel):
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    class_id: int

    class Config:
        orm_mode = True
