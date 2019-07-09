"""Mapping Global Data Sets: JSON Format"""
import json
filename = '16data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

#Let's make a list of all earthquakes.	
all_eq_dicts = all_eq_data['features']
#all_eq_dicts is a list, each item is a dictionary describing one earthquake.

#Let's extract magnitudes, location data, and location description.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	mags.append(mag)
	lon = eq_dict['geometry']['coordinates'][0]
	lons.append(lon)
	lat = eq_dict['geometry']['coordinates'][1]
	lats.append(lat)
	title = eq_dict['properties']['title']
	hover_texts.append(title)

#Let's build a world map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
data = [Scattergeo(lon=lons, lat=lats)]
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,#The above two approaches of assignment are equivalent.
	#Now let's change the marker size and color according to magnitude.
	'marker':{
		'size': [2*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar':{'title': 'Magnitude'},
	},
	#Let's add text description.
	'text': hover_texts,
}]
#Let's show available colorscales
from plotly import colors
for key in colors.PLOTLY_SCALES.keys():#colors.PLOTLY_SCALES is a dictionary.
	print(key)

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
