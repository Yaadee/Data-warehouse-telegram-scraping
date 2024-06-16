# from sqlalchemy.orm import Session
# import modelss, schemas

# def get_detection_result(db: Session, id: int):
#     return db.query(modelss.DetectionResult).filter(modelss.DetectionResult.id == id).first()

# def get_detection_results(db: Session, skip: int = 0):
#     return db.query(modelss.DetectionResult).offset(skip).all()

# def create_detection_result(db: Session, detection_result: schemas.DetectionResultCreate):
#     db_item = modelss.DetectionResult(**detection_result.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# def update_detection_result(db: Session, detection_id: int, detection_result: schemas.DetectionResultCreate):
#     db_detection = db.query(modelss.DetectionResult).filter(modelss.DetectionResult.id == detection_id).first()
#     if db_detection:
#         for key, value in detection_result.dict().items():
#             setattr(db_detection, key, value)
#         db.commit()
#         db.refresh(db_detection)
#     return db_detection

# def delete_detection_result(db: Session, detection_id: int):
#     db_detection = db.query(modelss.DetectionResult).filter(modelss.DetectionResult.id == detection_id).first()
#     if db_detection:
#         db.delete(db_detection)
#         db.commit()
#     return db_detection



from sqlalchemy.orm import Session
import modelss, schemas

def get_detection_result(db: Session, detection_id: int):
    return db.query(modelss.DetectionResult).filter(modelss.DetectionResult.id == detection_id).first()

def get_detection_results(db: Session, skip: int = 0):
    return db.query(modelss.DetectionResult).offset(skip).all()

def create_detection_result(db: Session, detection: schemas.DetectionResultCreate):
    db_detection = modelss.DetectionResult(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection

def update_detection_result(db: Session, detection_id: int, detection: schemas.DetectionResultCreate):
    db_detection = get_detection_result(db, detection_id)
    if db_detection is None:
        return None
    for key, value in detection.dict().items():
        setattr(db_detection, key, value)
    db.commit()
    db.refresh(db_detection)
    return db_detection

def delete_detection_result(db: Session, detection_id: int):
    db_detection = get_detection_result(db, detection_id)
    if db_detection is None:
        return None
    db.delete(db_detection)
    db.commit()
    return db_detection
