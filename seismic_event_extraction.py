from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import pandas as pd

# Initialize the IRIS client
client = Client("IRIS")

# Define the range of catalog
minlat = 29
maxlat = 32
minlon = 77
maxlon = 81
starttime = UTCDateTime("2010-01-01")
endtime = UTCDateTime("2020-01-01")
minmag = 0
maxmag = 10

# Fetch events from the ISC catalog
cat = client.get_events(starttime=starttime, endtime=endtime,
                        minlatitude=minlat, maxlatitude=maxlat,
                        minlongitude=minlon, maxlongitude=maxlon,
                        minmagnitude=minmag, maxmagnitude=maxmag,
                        mindepth=0, maxdepth=100,
                        catalog="ISC")

# Prepare a list to store event details
event_data = []

# Loop through the events and extract relevant information
for event in cat:
    origin = event.preferred_origin() or event.origins[0]
    magnitude = event.preferred_magnitude() or event.magnitudes[0]

    # Extract latitude, longitude, magnitude, depth, and origin time
    lat = origin.latitude
    lon = origin.longitude
    mag = magnitude.mag
    depth = origin.depth / 1000 if origin.depth is not None else None  # Convert depth to kilometers
    origin_time = origin.time  # UTCDateTime

    # Append the event data (origin_time, lat, lon, mag, depth) to the list
    event_data.append([origin_time, lat, lon, mag, depth])

# Convert the list to a Pandas DataFrame
df = pd.DataFrame(event_data, columns=["Origin Time", "Latitude", "Longitude", "Magnitude", "Depth"])

# Save the DataFrame to a CSV file
df.to_csv("./seismic_events.csv", index=False)

# Print the DataFrame
print(df)
