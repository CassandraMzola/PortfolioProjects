# Earthquake Data Pipeline

The **Earthquake Data Pipeline** automatically collects live earthquake data from the **USGS (United States Geological Survey)** and stores it in **Google BigQuery**. This enables both **real-time** and **historical analysis** of earthquakes for research or data projects.  

## Pipeline Components

- **Python script:** `earthquake_project.py` – fetches, cleans, and uploads earthquake data.  
- **Jupyter Notebook:** `earthquake_project.ipynb` – for exploration and testing.  
- **Dependencies:** Listed in `requirements.txt`.  

## Data Source

- **API:** [USGS Earthquake GeoJSON Feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)  
- **Frequency:** Every hour (can be scheduled via GitHub Actions or other schedulers)  
- **Data Collected:** Timestamp, location, magnitude, longitude, latitude, depth  

## BigQuery Storage

- **Project ID:** `earthquake-project-469810`  
- **Dataset:** `earthquake_dataset`  
- **Table:** `earthquakes`  
- **Upload Mode:** Append (new records are added each run)  

## Requirements

Python packages (install via `requirements.txt`):  
- pandas  
- requests  
- google-cloud-bigquery  
- pandas-gbq  

## Usage

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/Earthquake-Data-Pipeline.git
cd Earthquake-Data-Pipeline

Set up Google Cloud credentials

export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/key.json"


Install dependencies

pip install -r requirements.txt


Run the pipeline

python src/earthquake_project.py

Optional: Automation

Automate the pipeline with GitHub Actions or any scheduler to run at your desired frequency (e.g., hourly). The workflow checks out the repo, installs dependencies, and runs the script automatically.

Folder Structure
Earthquake-Data-Pipeline/
├── src/
│   ├── earthquake_project.py
│   └── earthquake_project.ipynb
├── requirements.txt
└── README.md

