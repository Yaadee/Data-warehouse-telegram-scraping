import pandas as pd
import os
from loguru import logger

# Set up logging
logger.add("logs/app.log", rotation="1 MB")

def clean_data(input_path, output_path):
    df = pd.read_json(input_path)
    df.drop_duplicates(inplace=True)
    df.fillna('Unknown', inplace=True)
    df.to_json(output_path, orient='records')
    logger.info(f"Cleaned data saved to {output_path}")

def main():
    raw_data_files = os.listdir('data/raw')
    for file in raw_data_files:
        input_path = os.path.join('data', 'raw', file)
        output_path = os.path.join('data', 'cleaned', file)
        logger.info(f"Cleaning data from {input_path}")
        clean_data(input_path, output_path)

if __name__ == "__main__":
    main()
