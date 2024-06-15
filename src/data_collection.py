import os
import json
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from datetime import datetime, timezone
from loguru import logger

# Configuration
api_id = '26622716'
api_hash = 'fd4274717bfcacf787cc15b9b51f1c76'
phone = '+251927463201'

# Define the channels for data collection and image scraping
data_channels = [
    'DoctorsET',
    'EAHCI',
    'yetenaweg'
]

image_channels = [
    'CheMed123',
    'lobelia4cosmetics'
]

# Directory to save collected data and images
DATA_DIR = 'data/raw'
IMAGE_DIR = os.path.join(DATA_DIR, 'telegram_images')

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

# Connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Helper function to make data JSON-serializable
def make_json_serializable(data):
    if isinstance(data, bytes):
        return data.decode('utf-8', errors='ignore')
    elif isinstance(data, datetime):
        return data.isoformat()
    elif isinstance(data, dict):
        return {k: make_json_serializable(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [make_json_serializable(v) for v in data]
    else:
        return data

# Function to collect data
async def collect_data(channel):
    messages = await client.get_messages(channel)
    data = []
    for message in messages:
        msg_dict = message.to_dict()
        msg_dict = make_json_serializable(msg_dict)
        data.append(msg_dict)
    return data

# Function to save data
def save_data(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, default=str)
    logger.info(f"Saved data to {path}")

# Function to download images
async def download_images(channel, start_date=None, end_date=None):
    channel_image_dir = os.path.join(IMAGE_DIR, channel)
    os.makedirs(channel_image_dir, exist_ok=True)
    
    async for message in client.iter_messages(channel, filter=InputMessagesFilterPhotos):
        message_date = message.date.replace(tzinfo=timezone.utc)  # Make message date timezone aware
        if (start_date and message_date < start_date) or (end_date and message_date > end_date):
            continue
        # Download the photo
        await client.download_media(message.photo, file=os.path.join(channel_image_dir, f'{message.id}.jpg'))
    logger.info(f"Downloaded images from {channel}")

def main():
    with client:
        # Data collection
        for channel in data_channels:
            logger.info(f"Collecting data from {channel}")
            data = client.loop.run_until_complete(collect_data(channel))
            data_path = os.path.join(DATA_DIR, f"{channel}.json")
            save_data(data, data_path)
        
        # Image scraping
        for channel in image_channels:
            logger.info(f"Downloading images from {channel}")
            client.loop.run_until_complete(download_images(
                channel, 
                start_date=datetime(2022, 5, 1, tzinfo=timezone.utc), 
                end_date=datetime(2024, 6, 10, tzinfo=timezone.utc)
            ))

if __name__ == "__main__":
    main()
