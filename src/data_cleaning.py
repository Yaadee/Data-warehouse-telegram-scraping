# import pandas as pd
# import os
# from loguru import logger

# # Set up logging
# logger.add("logs/app.log", rotation="1 MB")

# def clean_data(input_path, output_path):
#     df = pd.read_json(input_path)
#     df.drop_duplicates(inplace=True)
#     df.fillna('Unknown', inplace=True)
#     df.to_json(output_path, orient='records')
#     logger.info(f"Cleaned data saved to {output_path}")

# def main():
#     raw_data_files = os.listdir('data/raw')
#     for file in raw_data_files:
#         input_path = os.path.join('data', 'raw', file)
#         output_path = os.path.join('data', 'cleaned', file)
#         logger.info(f"Cleaning data from {input_path}")
#         clean_data(input_path, output_path)

# if __name__ == "__main__":
#     main()


import os
import json
import pandas as pd
from loguru import logger

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

# Directory paths
RAW_DATA_DIR = 'data/raw'
CLEANED_DATA_DIR = 'data/cleaned'

# Create directories if they don't exist
os.makedirs(CLEANED_DATA_DIR, exist_ok=True)

# Function to flatten lists and dictionaries
def flatten_column(data):
    if isinstance(data, dict):
        return json.dumps(data)
    elif isinstance(data, list):
        return json.dumps(data)
    else:
        return data

# Function to clean data
def clean_data(file_path, channel_name):
    try:
        # Load data
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Flatten lists and dictionaries
        df = df.applymap(flatten_column)
        
        # Remove duplicates
        df.drop_duplicates(inplace=True)
        
        # Handle missing values (example: fill with None)
        df.fillna('None', inplace=True)
        
        # Standardize formats (example: convert all text to lowercase)
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].apply(lambda x: x.lower() if isinstance(x, str) else x)
        
        # Data validation (example: ensure 'date' is a datetime)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Save cleaned data
        cleaned_file_path = os.path.join(CLEANED_DATA_DIR, f"{channel_name}_cleaned.json")
        df.to_json(cleaned_file_path, orient='records')
        
        logger.info(f"Cleaned data saved to {cleaned_file_path}")
    except Exception as e:
        logger.error(f"Error cleaning data from {file_path}: {e}")

def main():
    for file_name in os.listdir(RAW_DATA_DIR):
        file_path = os.path.join(RAW_DATA_DIR, file_name)
        if os.path.isfile(file_path) and file_path.endswith('.json'):
            channel_name = os.path.splitext(file_name)[0]
            clean_data(file_path, channel_name)

if __name__ == "__main__":
    main()
