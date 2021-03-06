import settings
import const
from src import util
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Access default configurations
config = settings.config[const.DEFAULT]

# Turn off plot interactive mode to let IDE display the plots
plt.interactive(False)

# Read stations
stations = pd.read_csv(config[const.BJ_STATIONS], delimiter=';', low_memory=False)

# Read cleaned data, append station data
df = pd.read_csv(config[const.BJ_OBSERVED], delimiter=';', low_memory=False)
df = df.merge(stations, how='left', on=[const.ID], suffixes=['_obs', '_st'])
df = util.merge_columns(df, main='_obs', auxiliary='_st')

fig, axes = plt.subplots()

# Plot station positions
for station_type, group in stations.groupby(['station_type']):
    axes.plot(group['latitude'], group['longitude'], 'o', label=station_type)
axes.legend()

# Write station names close to their position

for s, name in enumerate(stations['station_id']):
    axes.annotate(name, (stations.loc[s, 'latitude'], stations.loc[s, 'longitude']))


# Averages per station
# average columns over each station
aggDf = df.groupby('station_id', as_index=False).agg({'longitude': 'first', 'latitude': 'first',
                                                     'temperature': 'mean', 'humidity': 'mean',
                                                     'wind_direction': 'mean', 'wind_speed': 'mean',
                                                     'pressure': 'mean', 'PM2.5': 'mean', 'PM10': 'mean',
                                                     'O3': 'mean'})

fig1, axes1 = plt.subplots(nrows=1, ncols=3, figsize=(15, 3))
fig2, axes2 = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))

scale = 500  # multiplier scale for enlarging plotted circles

# plot normalized PM2.5 per station
aggDf.plot.scatter(x='latitude', y='longitude',
                   s=util.normalize(aggDf['PM2.5'], scale), title='PM2.5', fontsize=13, ax=axes1[0])

# plot normalized PM10 per station
aggDf.plot.scatter(x='latitude', y='longitude',
                   s=util.normalize(aggDf['PM10'], scale), title='PM10', fontsize=13, ax=axes1[1])

# plot normalized O3 per station
aggDf.plot.scatter(x='latitude', y='longitude',
                   s=util.normalize(aggDf['O3'], scale), title='O3', fontsize=13, ax=axes1[2])

# plot normalized temperature per station
aggDf.plot.scatter(x='latitude', y='longitude',
                   s=util.normalize(aggDf['temperature'], scale), title='temperature', fontsize=13, ax=axes2[0])

# plot normalized humidity per station
aggDf.plot.scatter(x='latitude', y='longitude',
                   s=util.normalize(aggDf['humidity'], scale), title='humidity', fontsize=13, ax=axes2[1])

# plot wind vector field per station
windRadian = np.radians(270 - aggDf['wind_direction'])  # degree 0 means north -> south, so it must be replaced with 270
windSpeed = util.normalize(aggDf['wind_speed'], 10)
plt.figure()
plt.title('Wind vector field')
plt.quiver(aggDf['latitude'], aggDf['longitude'], np.cos(windRadian),
           np.sin(windRadian), windSpeed, units='width', pivot='mid', color='g')
plt.xlabel('latitude')
plt.ylabel('longitude')

plt.show()
