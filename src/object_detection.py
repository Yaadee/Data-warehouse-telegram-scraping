
import torch
import os
import json
from loguru import logger

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

# Load YOLO model from local path
model = torch.hub.load('./yolov5', 'custom', path='yolov5s.pt', source='local')

def detect_objects(image_path):
    results = model(image_path)
    detections = results.xyxy[0].cpu().numpy().tolist()
    return detections

def save_detections(detections, path):
    with open(path, 'w') as f:
        json.dump(detections, f)
    logger.info(f"Saved detection results to {path}")

def process_images_from_directory(images_dir, detections_dir):
    os.makedirs(detections_dir, exist_ok=True)
    for img_file in os.listdir(images_dir):
        img_path = os.path.join(images_dir, img_file)
        detections = detect_objects(img_path)
        detection_path = os.path.join(detections_dir, f"{os.path.splitext(img_file)[0]}.json")
        save_detections(detections, detection_path)

def main():
    directories = [
        ('data/raw/telegram_images/lobelia4cosmetics', 'data/detections/lobelia4cosmetics'),
        ('data/raw/telegram_images/CheMed123', 'data/detections/CheMed123')
    ]
    
    for images_dir, detections_dir in directories:
        process_images_from_directory(images_dir, detections_dir)

if __name__ == "__main__":
    main()
