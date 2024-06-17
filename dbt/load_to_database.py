import pandas as pd
from sqlalchemy import create_engine
import json
DB_CONNECTION_STRING = 'postgresql://postgres:admin@localhost/Data-warehouse'

# Function to load JSON data into a DataFrame
def load_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        df = pd.json_normalize(data)  # Flatten nested JSON into DataFrame
    return df

# Load JSON files into Pandas DataFrames
doctors_df = load_data('dbt/data/cleaned/DoctorsET_cleaned.json')
eahci_df = load_data('dbt/data/cleaned/EAHCI_cleaned.json')
lobelia4_df = load_data('dbt/data/cleaned/lobelia4cosmetics_cleaned.json')
yetenaweg_df = load_data('dbt/data/cleaned/yetenaweg_cleaned.json')

# Database engine
engine = create_engine(DB_CONNECTION_STRING)

# Function to handle serialization of problematic columns
def serialize_data(df):
    # Example: serialize 'message' column as JSON string
    if 'message' in df.columns:
        df['message'] = df['message'].apply(json.dumps)
    return df

# Serialize problematic columns (if needed)
doctors_df = serialize_data(doctors_df)

# Load DataFrames into PostgreSQL database
try:
    doctors_df.to_sql('doctorset_raw', engine, if_exists='replace', index=False)
    eahci_df.to_sql('eahci_raw', engine, if_exists='replace', index=False)
    lobelia4_df.to_sql('lobelia4_raw', engine, if_exists='replace', index=False)
    yetenaweg_df.to_sql('yetenaweg_raw', engine, if_exists='replace', index=False)
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data to database: {e}")

