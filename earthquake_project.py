import requests
import pandas as pd
from google.cloud import bigquery
from pandas_gbq import to_gbq


# Authenticate with service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
client = bigquery.Client(project="earthquake-project-469810")

# Pull JSON data from USGS
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)
data = response.json()

# Flatten JSON
earthquakes = pd.json_normalize(data['features'])

# Keep important columns
earthquakes = earthquakes[['properties.time','properties.place','properties.mag','geometry.coordinates']]

# Split coordinates
earthquakes[['longitude','latitude','depth']] = pd.DataFrame(
    earthquakes['geometry.coordinates'].tolist(), index=earthquakes.index
)

# Drop original column & rename
earthquakes.drop(columns=['geometry.coordinates'], inplace=True)
earthquakes.rename(columns={
    'properties.time': 'time',
    'properties.place': 'place',
    'properties.mag': 'magnitude'
}, inplace=True)

# Convert timestamp to datetime
earthquakes['time'] = pd.to_datetime(earthquakes['time'], unit='ms')

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

