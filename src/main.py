# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine, get_db
# import crud, modelss, schemas
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine, get_db
# import crud, modelss, schemas

# modelss.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Ethio Medical Business Data Warehouse API"}

# @app.post("/detections/", response_model=schemas.DetectionResult)
# def create_detection_result(detection: schemas.DetectionResultCreate, db: Session = Depends(get_db)):
#     return crud.create_detection_result(db=db, detection=detection.dict())

# @app.get("/detections/{detection_id}", response_model=schemas.DetectionResult)
# def read_detection_result(detection_id: int, db: Session = Depends(get_db)):
#     db_detection = crud.get_detection_result(db, detection_id)
#     if db_detection is None:
#         raise HTTPException(status_code=404, detail="Detection not found")
#     return db_detection

# @app.get("/detections/", response_model=list[schemas.DetectionResult])
# def read_detection_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     detections = crud.get_detection_results(db, skip=skip, limit=limit)
#     return detections

# @app.put("/detections/{detection_id}", response_model=schemas.DetectionResult)
# def update_detection_result(detection_id: int, detection: schemas.DetectionResultCreate, db: Session = Depends(get_db)):
#     db_detection = crud.update_detection_result(db, detection_id, detection.dict())
#     if db_detection is None:
#         raise HTTPException(status_code=404, detail="Detection not found")
#     return db_detection

# @app.delete("/detections/{detection_id}", response_model=schemas.DetectionResult)
# def delete_detection_result(detection_id: int, db: Session = Depends(get_db)):
#     db_detection = crud.delete_detection_result(db, detection_id)
#     if db_detection is None:
#         raise HTTPException(status_code=404, detail="Detection not found")
#     return db_detection

from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, modelss, schemas
from database import SessionLocal, engine

modelss.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model=List[schemas.DetectionResult])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
