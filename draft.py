python -m venv .venv
source .venv/bin/activate
import pandas as pd
import folium

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/berkleys/Documents/Github-repository/DATA205-berkleysayaka/Capstone project/lar2018_100000.csv')

# Filter the DataFrame for VA, MD, and DC
##filtered_df = df[df['state'].isin(['VA', 'MD', 'DC'])]

# Create a map centered around the region
#map_center = [38.9072, -77.0369]  # Latitude and Longitude for Washington, DC
#mymap = folium.Map(location=map_center, zoom_start=7)

# Add points to the map
#for index, row in filtered_df.iterrows():
   # folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Application ID: {row['application_id']}",
    ).add_to(mymap)

# Save the map to an HTML file
#mymap.save('applications_map.html')


print(df.head)

df = pd.read_csv('/Users/berkleys/Documents/Github-repository/DATA205-berkleysayaka/Capstone project/lar2018_100000.csv')
