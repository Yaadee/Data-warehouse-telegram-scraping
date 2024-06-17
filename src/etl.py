import os
import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import DetectionResult
from loguru import logger

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

def load_detection_results(detection_results, image_id, db: Session):
    for index, detection in enumerate(detection_results):
        if isinstance(detection, list) and len(detection) == 6:
            x_min, y_min, x_max, y_max, confidence, class_id = detection
            class_name = get_class_name(class_id)

            db_result = DetectionResult(
                image_id=image_id,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                confidence=confidence,
                class_id=class_id,
                class_name=class_name
            )
            db.add(db_result)
        else:
            logger.error(f"Unexpected detection format in image {image_id}: {detection}")

    db.commit()

def get_class_name(class_id):
    # Example mapping of class_id to class_name
    class_mapping = {
        32: "example_class",  # Adjusted to match integer type if your class_id is integer in database
        # Add other mappings as needed
    }
    return class_mapping.get(class_id, "unknown")

def process_detection_files(directory, db):
    for detection_file in os.listdir(directory):
        detection_path = os.path.join(directory, detection_file)
        with open(detection_path, 'r') as f:
            try:
                detection_results = json.load(f)
                if isinstance(detection_results, list):
                    image_id = os.path.splitext(detection_file)[0]
                    load_detection_results(detection_results, image_id, db)
                else:
                    logger.error(f"Unexpected JSON structure in file {detection_file}")
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing JSON in file {detection_file}: {e}")

def main():
    db = SessionLocal()
    directories = ['data/detections/CheMed123', 'data/detections/lobelia4cosmetics']

    for directory in directories:
        process_detection_files(directory, db)

    db.close()

if __name__ == "__main__":
    main()
