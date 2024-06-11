

import os
import requests
from bs4 import BeautifulSoup
from telethon.sync import TelegramClient
import pandas as pd
from loguru import logger

api_id = '26622716'
api_hash = 'fd4274717bfcacf787cc15b9b51f1c76'
channels = [
    'https://t.me/DoctorsET',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/EAHCI',
    'https://t.me/yetenaweg',
    'https://et.tgstat.com/medicine'
]

image_channels = [
    'https://t.me/ChemedTelegramChannel',
    'https://t.me/lobelia4cosmetics'
]

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

def collect_data(client):
    for channel in channels:
        try:
            messages = []
            for message in client.iter_messages(channel, limit=100):
                messages.append({
                    'id': message.id,
                    'date': message.date.isoformat() if message.date else None,  # Convert datetime to ISO format string
                    'text': message.message,
                    'sender_id': message.sender_id,
                    'views': message.views
                })
            df = pd.DataFrame(messages)
            path = os.path.join('data', 'raw', f"{channel.split('/')[-1]}.json")
            df.to_json(path, orient='records')
            logger.info(f"Data collection complete for {channel}. Saved to {path}")
        except ValueError as e:
            logger.error(f"Error collecting data for {channel}: {e}")

def extract_image_urls(channel_url):
    try:
        response = requests.get(channel_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        image_urls = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and src.startswith('https://telegram.org/file/'):
                image_urls.append(src)
        return image_urls
    except Exception as e:
        logger.error(f"Error extracting image URLs from {channel_url}: {e}")
        return []

async def download_images(client, channel, image_urls, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for i, url in enumerate(image_urls):
            image_path = os.path.join(output_dir, f"image_{i}.jpg")
            await client.download_media(url, file=image_path)
            logger.info(f"Downloaded image {i+1}/{len(image_urls)} from {url}")
    except Exception as e:
        logger.error(f"Error downloading images: {e}")

async def scrape_images(client):
    for channel_url in image_channels:
        logger.info(f"Scraping images from {channel_url}")
        image_urls = extract_image_urls(channel_url)
        output_dir = os.path.join('data', 'images', os.path.basename(channel_url))
        await download_images(client, channel_url, image_urls, output_dir)

def main():
    with TelegramClient('session_name', api_id, api_hash) as client:
        if not os.path.exists('data/raw'):
            os.makedirs('data/raw')
        if not os.path.exists('data/images'):
            os.makedirs('data/images')
        collect_data(client)
        client.loop.run_until_complete(scrape_images(client))

if __name__ == "__main__":
    main()







import os
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from dotenv import load_dotenv
from datetime import datetime, timezone

# Load environment variables
load_dotenv()

# Configuration
api_id = '26622716'
api_hash = 'fd4274717bfcacf787cc15b9b51f1c76'
phone = '+251927463201'  # Corrected: Phone number must be a string with quotes

# Define the channels from which to download images
image_channels = [
    'lobelia4cosmetics',
    'CheMed123'
    # Add more channels if needed
]

# Directory to save images
SAVE_DIR = 'telegram_images'

# Create save directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Function to download images
async def download_images(channel, start_date=None, end_date=None, max_images=None):
    image_count = 0
    async for message in client.iter_messages(channel, filter=InputMessagesFilterPhotos):
        message_date = message.date.replace(tzinfo=timezone.utc)  # Make message date timezone aware
        if (start_date and message_date < start_date) or (end_date and message_date > end_date):
            continue
        if max_images and image_count >= max_images:
            break
        # Download the photo
        await client.download_media(message.photo, file=os.path.join(SAVE_DIR, f'{message.id}.jpg'))
        image_count += 1

def main():
    # Start the client
    with client:
        for channel in image_channels:
            # Run the function to download images from the channel
            client.loop.run_until_complete(download_images(channel, start_date=datetime(2024, 6, 1, tzinfo=timezone.utc), end_date=datetime(2024, 6, 10, tzinfo=timezone.utc), max_images=10))

if __name__ == "__main__":
    main()

