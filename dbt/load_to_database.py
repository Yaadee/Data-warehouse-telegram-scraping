import pandas as pd
from sqlalchemy import create_engine, types
import json
import os

# Database connection
engine = create_engine('postgresql://postgres:admin@localhost:5432/Data-warehouse')

# Print the current working directory
print("Current working directory:", os.getcwd())

# Paths to JSON files
json_files = {
    'doctorset_raw': 'dbt1/models/raw/DoctorsET.json',
    'eahci_raw': 'dbt1/models/raw/EAHCI.json',
    'yetenaweg_raw': 'dbt1/models/raw/yetenaweg.json',
    'lobelia4cosmetics_raw': 'dbt1/models/raw/lobelia4cosmetics.json'
}

# Function to read JSON file and infer schema
def infer_json_schema(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        if isinstance(json_data, list):  # Check if the JSON data is a list (array of objects)
            # Assuming each object in the array has the same structure, use the first object for schema inference
            sample_data = json_data[0]
        else:
            sample_data = json_data

        column_types = {
            col: types.VARCHAR(length=max(len(str(item)) for item in sample_data[col]))  # Infer VARCHAR length based on max length in sample
            for col in sample_data.keys()
        }
        return column_types

# Load JSON files into DataFrames and write to PostgreSQL
for table_name, file_path in json_files.items():
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        continue
    schema = infer_json_schema(file_path)
    df = pd.read_json(file_path, dtype=str, lines=True)
    df.to_sql(table_name, engine, if_exists='replace', index=False, dtype=schema)

print("Data loaded successfully into PostgreSQL.")
