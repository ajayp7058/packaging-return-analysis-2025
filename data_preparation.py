import pandas as pd
import geopandas as gpd

# Load GeoJSON boundary file
geo = gpd.read_file("geoBoundaries-ROU-ADM1_simplified.geojson")

# Load packaging return data
data = pd.read_excel("Total quantity_ianuary_July 2025.xlsx")  # or use pd.read_csv()

# Clean county names
geo["shapeName"] = geo["shapeName"].str.strip().str.lower()
data["County"] = data["County"].str.strip().str.lower()

# Merge datasets
merged = geo.merge(data, left_on="shapeName", right_on="County")
