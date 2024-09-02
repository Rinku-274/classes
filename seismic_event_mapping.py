import pandas as pd
import pygmt

# Read the CSV file
df = pd.read_csv("./seismic_events.csv")
topo_data = '@earth_relief_30s'

# Determine the min and max latitude and longitude
min_lat = df["Latitude"].min() - 0.1  # Subtract 1 degree
max_lat = df["Latitude"].max() + 0.1  # Add 1 degree
min_lon = df["Longitude"].min() - 0.1  # Subtract 1 degree
max_lon = df["Longitude"].max() + 0.1  # Add 1 degree
region = [min_lon, max_lon, min_lat, max_lat]  # [west, east, south, north]

# Create a simple map
fig = pygmt.Figure()
fig.grdimage(grid=topo_data, cmap="white", region=region, projection='M6i', shading = True, frame = True)

# Create a coastline map with calculated region

pygmt.makecpt(cmap="cool", series=[df.Depth.min(), df.Depth.max()], continuous=True)

# Plot the earthquake events

fig.plot(x=df.Longitude,y=df.Latitude,size=0.02*(2 **df.Magnitude),fill=df.Depth,cmap=True,style="cc",pen="black")
fig.colorbar(frame='af+lFocal Depth (km)')



# Show the map
fig.show()

# Save the figure to a file if needed
# fig.savefig("isc_events_map.png")
