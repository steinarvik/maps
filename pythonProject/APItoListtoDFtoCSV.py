import requests
import pandas as pd

# URL to get earthquake data from the past week (as an example)
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

# Request the data
response = requests.get(url)
data = response.json()

# Extract relevant information
earthquake_list = []
for feature in data['features']:
    properties = feature['properties']
    geometry = feature['geometry']
    earthquake_list.append([
        properties['mag'],
        properties['place'],
        geometry['coordinates'][1],  # Latitude
        geometry['coordinates'][0]   # Longitude
    ])

# Create a DataFrame
df = pd.DataFrame(earthquake_list, columns=['Magnitude', 'Location', 'Latitude', 'Longitude'])

# Save to CSV
csv_path = "earthquakes_real.csv"
df.to_csv(csv_path, index=False)