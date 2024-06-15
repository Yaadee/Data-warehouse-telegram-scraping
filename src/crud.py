from sqlalchemy.orm import Session
import modelss, schemas

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(modelss.DetectionResult).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = modelss.DetectionResult(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item









# def create_detection_result(db: Session, detection: dict):
#     db_result = DetectionResult(**detection, timestamp=datetime.utcnow())
#     db.add(db_result)
#     db.commit()
#     db.refresh(db_result)
#     return db_result

# def get_detection_result(db: Session, detection_id: int):
#     return db.query(DetectionResult).filter(DetectionResult.id == detection_id).first()

# def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(DetectionResult).offset(skip).limit(limit).all()

# def update_detection_result(db: Session, detection_id: int, detection_data: dict):
#     db_result = db.query(DetectionResult).filter(DetectionResult.id == detection_id).first()
#     if db_result:
#         for key, value in detection_data.items():
#             setattr(db_result, key, value)
#         db.add(db_result)
#         db.commit()
#         db.refresh(db_result)
#     return db_result

# def delete_detection_result(db: Session, detection_id: int):
#     db_result = db.query(DetectionResult).filter(DetectionResult.id == detection_id).first()
#     if db_result:
#         db.delete(db_result)
#         db.commit()
#     return db_result



# from sqlalchemy.orm import Session
# from datetime import datetime
# from typing import List 
# # from modelsss import DetectionResult
# import modelss

# import schemas


# def get_item(db: Session, item_id: int):
#     return db.query(modelss.Item).filter(modelss.Item.id == item_id).first()

# def get_items(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(modelss.Item).offset(skip).limit(limit).all()

# def create_item(db: Session, item: schemas.ItemCreate):
#     db_item = modelss.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


