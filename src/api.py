from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from loguru import logger

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/detection_results/", response_model=schemas.DetectionResult)
def create_detection_result(detection_result: schemas.DetectionResult, db: Session = Depends(get_db)):
    logger.info("Creating detection result")
    return crud.create_detection_result(db=db, detection_result=detection_result)

@app.get("/detection_results/", response_model=list[schemas.DetectionResult])
def read_detection_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info("Reading detection results")
    return crud.get_detection_results(db, skip=skip, limit=limit)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
