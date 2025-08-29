Earthquake Data Pipeline

Overview



The Earthquake Data Pipeline automatically collects live earthquake data from the USGS (United States Geological Survey) and stores it in Google BigQuery. This enables real-time and historical analysis of earthquakes for research or data projects.



The pipeline includes:



A Python script (earthquake\_project.py) that fetches and cleans earthquake data.



A Jupyter Notebook (earthquake\_project.ipynb) for exploration and testing.



A requirements.txt file specifying the necessary Python dependencies.



Data Source



API: USGS Earthquake GeoJSON Feed



Frequency: Every hour (can be scheduled via GitHub Actions or another scheduler).



Data pulled: Timestamp, location, magnitude, longitude, latitude, depth.



BigQuery Storage



Project ID: earthquake-project-469810



Dataset: earthquake\_dataset



Table: earthquakes



Upload mode: append (new records are added to the table each run)



Requirements



Python packages required (listed in requirements.txt):



pandas

requests

google-cloud-bigquery

pandas-gbq



Usage



Clone this repository.



Set up your Google Cloud service account and export credentials:



export GOOGLE\_APPLICATION\_CREDENTIALS="path/to/your/key.json"





Install dependencies:



pip install -r requirements.txt





Run the pipeline:



python src/earthquake\_project.py



Optional: Automation



The pipeline can be automated using GitHub Actions or any scheduler to run at your desired frequency (e.g., hourly). The workflow checks out the repo, installs dependencies, and runs the script automatically.



Folder Structure

Earthquake-Data-Pipeline/

│

├── src/

│   ├── earthquake\_project.py

│   └── earthquake\_project.ipynb

│

└── requirements.txt

