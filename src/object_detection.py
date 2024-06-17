# import torch
# import os
# import json
# from loguru import logger

# # Set up logging
# logger.add("logs/app.log", rotation="1 MB")

# # Load YOLO model from local path
# model = torch.hub.load('./yolov5', 'custom', path='yolov5s.pt', source='local')

# def detect_objects(image_path):
#     results = model(image_path)
#     detections = results.xyxy[0].cpu().numpy().tolist()
#     return detections

# def save_detections(detections, path):
#     with open(path, 'w') as f:
#         json.dump(detections, f)
#     logger.info(f"Saved detection results to {path}")

# def process_images_from_directory(images_dir, detections_dir):
#     os.makedirs(detections_dir, exist_ok=True)
#     for img_file in os.listdir(images_dir):
#         img_path = os.path.join(images_dir, img_file)
#         detections = detect_objects(img_path)
#         detection_path = os.path.join(detections_dir, f"{os.path.splitext(img_file)[0]}.json")
#         save_detections(detections, detection_path)

# def main():
#     directories = [
#         ('data/raw/telegram_images/lobelia4cosmetics', 'data/detections/lobelia4cosmetics'),
#         ('data/raw/telegram_images/CheMed123', 'data/detections/CheMed123')
#     ]
    
#     for images_dir, detections_dir in directories:
#         process_images_from_directory(images_dir, detections_dir)

# if __name__ == "__main__":
#     main()





import torch
import os
from pathlib import Path

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom

# Path to the folders
folders = ["/home/yadasa/Desktop/ethio-medical-business-data-warehouse/data/raw/telegram_images/lobelia4cosmetics", "/home/yadasa/Desktop/ethio-medical-business-data-warehouse/data/raw/telegram_images/CheMed123"]
base_path = "yolov5/data/telegram_images"

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    # Detect images in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            file_path = os.path.join(folder_path, file_name)
            # Inference
            results = model(file_path)
            # Save results
            save_path = Path("data/detections/results") / folder / file_name

            results.save(save_path)
result =model(file_path)






# import torch

# # Model
# model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom

# # Images
# img = "https://ultralytics.com/images/zidane.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# # Inference
# results = model(img)

# # Results
# results.show() # or .show(), .save(), .crop(), .pandas(), etc.