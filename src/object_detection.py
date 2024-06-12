import os
import json
from PIL import Image
from loguru import logger
import torch

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(image_path):
    try:
        results = model(image_path)
        detections = results.xyxy[0].cpu().numpy().tolist()
        return detections
    except Exception as e:
        logger.error(f"Error detecting objects in {image_path}: {e}")
        return None

def save_detections(detections, path):
    if detections:
        with open(path, 'w') as f:
            json.dump(detections, f)
        logger.info(f"Saved detection results to {path}")
    else:
        logger.warning(f"No detections found, skipping saving for {path}")

def main():
    images_dir = 'data/raw/telegram_images'
    detections_dir = 'data/detections'
    os.makedirs(detections_dir, exist_ok=True)

    for img_file in os.listdir(images_dir):
        img_path = os.path.join(images_dir, img_file)
        if os.path.isfile(img_path):
            detections = detect_objects(img_path)
            if detections:
                detection_path = os.path.join(detections_dir, f"{os.path.splitext(img_file)[0]}.json")
                save_detections(detections, detection_path)
        else:
            logger.warning(f"{img_path} is a directory, skipping...")

if __name__ == "__main__":
    main()
