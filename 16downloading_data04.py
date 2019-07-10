"""World Fires"""
import csv
filename = '16data/world_fires_7_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	next(reader)	
	lats, lons, brts, dates = [], [], [], []
	for row in reader:
		try:
			lats.append(float(row[0]))
			lons.append(float(row[1]))
			brts.append(float(row[2]))
			dates.append(row[5])
		except IndexError:
			print("an incomplete input line.")
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
data=[{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'marker':{
		'size': [0.015*brt for brt in brts],
		'color': brts,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Brightness'},
	},
	'text': dates,
}]
my_layout = Layout(title='Global Fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
