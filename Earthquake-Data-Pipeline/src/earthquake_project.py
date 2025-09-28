import requests
import pandas as pd
import os
from google.cloud import bigquery
from pandas_gbq import to_gbq

# Authenticate with service account
client = bigquery.Client(project="earthquake-project-469810")

# Pull JSON data from USGS
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)
data = response.json()

# Flatten JSON
earthquakes = pd.json_normalize(data['features'])

# Debug: show all available columns from USGS
print("Available columns:", earthquakes.columns.tolist())

# Define expected columns and filter only those that exist
cols_to_keep = [col for col in [
    'properties.time', 'properties.place', 'properties.mag', 'geometry.coordinates'
] if col in earthquakes.columns]

earthquakes = earthquakes[cols_to_keep]

# Split coordinates safely
if 'geometry.coordinates' in earthquakes.columns:
    earthquakes[['longitude', 'latitude', 'depth']] = pd.DataFrame(
        earthquakes['geometry.coordinates'].tolist(), index=earthquakes.index
    )
    earthquakes.drop(columns=['geometry.coordinates'], inplace=True)

# Rename columns
rename_map = {
    'properties.time': 'time',
    'properties.place': 'place',
    'properties.mag': 'magnitude'
}
earthquakes.rename(columns={k: v for k, v in rename_map.items() if k in earthquakes.columns}, inplace=True)

# Convert timestamp if available
if 'time' in earthquakes.columns:
    earthquakes['time'] = pd.to_datetime(earthquakes['time'], unit='ms', errors='coerce')

print("\nCleaned DataFrame preview:")
print(earthquakes.head())

# Upload to BigQuery
dataset_id = "earthquake_dataset"
table_id = "earthquakes"

to_gbq(
    dataframe=earthquakes,
    destination_table=f"{dataset_id}.{table_id}",
    project_id="earthquake-project-469810",
    if_exists="append"
)

print("Upload complete!")

