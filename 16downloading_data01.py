"""csv file format"""
#In a csv file, every field is a string, so numbers should be converted by
#int() or float() before use.
#In a json file, contents are stored in dictionary or list, so numbers can be
#used directly.
import csv
from datetime import datetime
#This imports the datetime class from the datetime module.
filename = '16data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
#The csv.reader() requires a file object, and returns a reader object.
	header_row = next(reader)
#The next() requires a reader object, and returns a list containing information
#about the next line in the file. Each item in the list is a field of the line
	print(header_row)
	
	for index, column_header in enumerate(header_row):
#The enumerate() function returns both the index of each item and the value
#of each item as you loop through a list.
		print(index, column_header)
	
#Let's extract dates, high temperatures, and low temperatures.
	dates, highs, lows = [], [], []
	for row in reader:#This loops through the remaining rows in the file.
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
#strptime() requires two arguments. The first is the string to be converted.
#The second is the format of the string.
#current_date could be something like <2018-07-01 00:00:00>
		try:
			high = int(row[5])#cannot convert an empty string to int.
			low = int(row[6])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
#If one line of csv file is missing data, we just discard this line.
			
import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
#alpha=0 is transparent. alpha=1(the default) is opaque.
ax.plot(dates, lows, c='blue', alpha=0.5)#Two plots in the same graph.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#the fill_between() method, which takes a series of x-values and two
#series of y-values, can fill the space between the two y-value series.

plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
#The call to fig.autofmt_xdate() draws the x labels diagonally to prevent
#them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
