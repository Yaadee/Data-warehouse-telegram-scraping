import torch
import os
import json
from PIL import Image
from loguru import logger

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(image_path):
    results = model(image_path)
    detections = results.xyxy[0].cpu().numpy().tolist()
    return detections

def save_detections(detections, path):
    with open(path, 'w') as f:
        json.dump(detections, f)
    logger.info(f"Saved detection results to {path}")

def main():
    images_dir = 'data/images'
    detections_dir = 'data/detections'
    os.makedirs(detections_dir, exist_ok=True)

    for img_file in os.listdir(images_dir):
        img_path = os.path.join(images_dir, img_file)
        detections = detect_objects(img_path)
        detection_path = os.path.join(detections_dir, f"{os.path.splitext(img_file)[0]}.json")
        save_detections(detections, detection_path)

if __name__ == "__main__":
    main()
