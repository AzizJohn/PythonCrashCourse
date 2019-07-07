#Roll two dice
from random import randint
from plotly.graph_objs import Bar, Layout #two classes
from plotly import offline
class Die:
	def __init__(self, num_sides=6):
		self.num_sides = num_sides
	def roll(self):
		return randint(1, self.num_sides)

die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]#put Bar() inside brackets.
#class Bar() represents a data set that will be formatted as a bar chart.
x_axis_config = {'title': 'Result', 'dtick': 1}
#The 'dtick': 1 setting tells Plotly to label every tick mark.
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
	xaxis=x_axis_config, yaxis=y_axis_config)
#Layout() class returns an object that specifies the layout and configuration
#of the graph as a whole.
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
#The function offline.plot() needs a dictionary containing the data and layout
#objects, and it also accepts a name for the file where the graph will be
#saved.
