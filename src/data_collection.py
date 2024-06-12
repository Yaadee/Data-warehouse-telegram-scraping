

# import os
# import requests
# from bs4 import BeautifulSoup
# from telethon.sync import TelegramClient
# import pandas as pd
# from loguru import logger

# api_id = '26622716'
# api_hash = 'fd4274717bfcacf787cc15b9b51f1c76'
# channels = [
#     'https://t.me/DoctorsET',
#     'https://t.me/lobelia4cosmetics',
#     'https://t.me/EAHCI',
#     'https://t.me/yetenaweg',
#     'https://et.tgstat.com/medicine'
# ]

# image_channels = [
#     'https://t.me/ChemedTelegramChannel',
#     'https://t.me/lobelia4cosmetics'
# ]

# # Set up logging
# logger.add("logs/app.log", rotation="1 MB")

# def collect_data(client):
#     for channel in channels:
#         try:
#             messages = []
#             for message in client.iter_messages(channel, limit=100):
#                 messages.append({
#                     'id': message.id,
#                     'date': message.date.isoformat() if message.date else None,  # Convert datetime to ISO format string
#                     'text': message.message,
#                     'sender_id': message.sender_id,
#                     'views': message.views
#                 })
#             df = pd.DataFrame(messages)
#             path = os.path.join('data', 'raw', f"{channel.split('/')[-1]}.json")
#             df.to_json(path, orient='records')
#             logger.info(f"Data collection complete for {channel}. Saved to {path}")
#         except ValueError as e:
#             logger.error(f"Error collecting data for {channel}: {e}")

# def extract_image_urls(channel_url):
#     try:
#         response = requests.get(channel_url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         image_urls = []
#         for img in soup.find_all('img'):
#             src = img.get('src')
#             if src and src.startswith('https://telegram.org/file/'):
#                 image_urls.append(src)
#         return image_urls
#     except Exception as e:
#         logger.error(f"Error extracting image URLs from {channel_url}: {e}")
#         return []

# async def download_images(client, channel, image_urls, output_dir):
#     try:
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)
#         for i, url in enumerate(image_urls):
#             image_path = os.path.join(output_dir, f"image_{i}.jpg")
#             await client.download_media(url, file=image_path)
#             logger.info(f"Downloaded image {i+1}/{len(image_urls)} from {url}")
#     except Exception as e:
#         logger.error(f"Error downloading images: {e}")

# async def scrape_images(client):
#     for channel_url in image_channels:
#         logger.info(f"Scraping images from {channel_url}")
#         image_urls = extract_image_urls(channel_url)
#         output_dir = os.path.join('data', 'images', os.path.basename(channel_url))
#         await download_images(client, channel_url, image_urls, output_dir)

# def main():
#     with TelegramClient('session_name', api_id, api_hash) as client:
#         if not os.path.exists('data/raw'):
#             os.makedirs('data/raw')
#         if not os.path.exists('data/images'):
#             os.makedirs('data/images')
#         collect_data(client)
#         client.loop.run_until_complete(scrape_images(client))

# if __name__ == "__main__":
#     main()







# import os
# from telethon.sync import TelegramClient
# from telethon.tl.types import InputMessagesFilterPhotos
# from dotenv import load_dotenv
# from datetime import datetime, timezone

# # Load environment variables
# load_dotenv()

# # Configuration
# api_id = '26622716'
# api_hash = 'fd4274717bfcacf787cc15b9b51f1c76'
# phone = '+251927463201'  # Corrected: Phone number must be a string with quotes

# # Define the channels from which to download images
# image_channels = [
#     'lobelia4cosmetics',
#     'CheMed123'
#     # Add more channels if needed
# ]

# # Directory to save images
# SAVE_DIR = 'telegram_images'

# # Create save directory if it doesn't exist
# os.makedirs(SAVE_DIR, exist_ok=True)

# # Connect to Telegram
# client = TelegramClient('session_name', api_id, api_hash)

# # Function to download images
# async def download_images(channel, start_date=None, end_date=None, max_images=None):
#     image_count = 0
#     async for message in client.iter_messages(channel, filter=InputMessagesFilterPhotos):
#         message_date = message.date.replace(tzinfo=timezone.utc)  # Make message date timezone aware
#         if (start_date and message_date < start_date) or (end_date and message_date > end_date):
#             continue
#         if max_images and image_count >= max_images:
#             break
#         # Download the photo
#         await client.download_media(message.photo, file=os.path.join(SAVE_DIR, f'{message.id}.jpg'))
#         image_count += 1

# def main():
#     # Start the client
#     with client:
#         for channel in image_channels:
#             # Run the function to download images from the channel
#             client.loop.run_until_complete(download_images(channel, start_date=datetime(2024, 6, 1, tzinfo=timezone.utc), end_date=datetime(2024, 6, 10, tzinfo=timezone.utc), max_images=10))

# if __name__ == "__main__":
#     main()





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
async def collect_data(channel, limit=100):
    messages = await client.get_messages(channel, limit=limit)
    data = []
    for message in messages:
        msg_dict = message.to_dict()
        msg_dict = make_json_serializable(msg_dict)
        data.append(msg_dict)
    return data

# Function to save data
def save_data(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)
    logger.info(f"Saved data to {path}")

# Function to download images
async def download_images(channel, start_date=None, end_date=None, max_images=None):
    channel_image_dir = os.path.join(IMAGE_DIR, channel)
    os.makedirs(channel_image_dir, exist_ok=True)
    
    image_count = 0
    async for message in client.iter_messages(channel, filter=InputMessagesFilterPhotos):
        message_date = message.date.replace(tzinfo=timezone.utc)  # Make message date timezone aware
        if (start_date and message_date < start_date) or (end_date and message_date > end_date):
            continue
        if max_images and image_count >= max_images:
            break
        # Download the photo
        await client.download_media(message.photo, file=os.path.join(channel_image_dir, f'{message.id}.jpg'))
        image_count += 1
    logger.info(f"Downloaded {image_count} images from {channel}")

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
                end_date=datetime(2024, 6, 10, tzinfo=timezone.utc), 
                max_images=20
            ))

if __name__ == "__main__":
    main()
