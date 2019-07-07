#Roll a die.
"""
$ python3 -m pip install --user plotly
"""
from random import randint
from plotly.graph_objs import Bar, Layout #two classes
from plotly import offline
class Die:
	def __init__(self, num_sides=6):
		self.num_sides = num_sides
	def roll(self):
		return randint(1, self.num_sides)

die = Die()
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
x_values = list(range(1, die.num_sides+1))#[1,2,3,4,5,6]
data = [Bar(x=x_values, y=frequencies)]#put Bar() inside brackets.
#class Bar() represents a data set that will be formatted as a bar chart.
x_axis_config = {'title': 'Result'}#a dictionary
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
	xaxis=x_axis_config, yaxis=y_axis_config)
#Layout() class returns an object that specifies the layout and configuration
#of the graph as a whole.
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
#The function offline.plot() needs a dictionary containing the data and layout
#objects, and it also accepts a name for the file where the graph will be
#saved.
