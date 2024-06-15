
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List 
from modelss import DetectionResult


def create_detection_result(db: Session, detection: dict):
    db_result = DetectionResult(**detection, timestamp=datetime.utcnow())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_detection_result(db: Session, detection_id: int):
    return db.query(DetectionResult).filter(DetectionResult.id == detection_id).first()

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DetectionResult).offset(skip).limit(limit).all()

def update_detection_result(db: Session, detection_id: int, detection_data: dict):
    db_result = db.query(DetectionResult).filter(DetectionResult.id == detection_id).first()
    if db_result:
        for key, value in detection_data.items():
            setattr(db_result, key, value)
        db.add(db_result)
        db.commit()
        db.refresh(db_result)
    return db_result

def delete_detection_result(db: Session, detection_id: int):
    db_result = db.query(DetectionResult).filter(DetectionResult.id == detection_id).first()
    if db_result:
        db.delete(db_result)
        db.commit()
    return db_result

