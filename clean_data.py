import pandas as pd
import time
from geopy.geocoders import Nominatim

""" transforme CSV to dataframe  """
df = pd.read_csv("data.csv")

""" departement --> LAT-LON """
latitude = []
longitude = []
new = df[['departement']]
df2 = new.drop_duplicates(subset=['departement'])
df2 = df2.reset_index()
df2 = df2.drop(columns=['index'])
lat = []
lon = []

for row in df2.itertuples(index=False):
    for name in row:
        time.sleep(0.5)
        word = "NULL"
        try:
            address = name
            geolocator = Nominatim(user_agent="Your_Name")
            location = geolocator.geocode(address)
            lat.append(location.latitude)
            lon.append(location.longitude)
        except:
            lat.append(word)
            lon.append(word)

df2['lat'] = pd.DataFrame(lat)
df2['lon'] = pd.DataFrame(lon)

departement_lat_lon = df2.rename(columns={'departement': 'departement', 'lat': 'latitude', 'lon': 'longitude'})
print(departement_lat_lon)
