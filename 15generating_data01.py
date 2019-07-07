"""
$ sudo apt install python3-pip
$ python3 -m pip install --user matplotlib
"""

import matplotlib.pyplot as plt #pyplot is a module
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

print(plt.style.available)#prints available styles.
plt.style.use('seaborn')
#You shouldd call style.use function before subplots function.
fig, ax = plt.subplots()
#The subplots() function can generate one or more plots in the same figure.
#The variable fig represents the entire figure or collection of plots that are
#generated.
#The variable ax represents a single plot in the figure.

ax.plot(input_values, squares, linewidth=3)#Draw a plot.
ax.scatter(2, 4, s=200) #Draw a scatter point. <s> is size of the marker.

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
ax.scatter(x_values, y_values, c='red', s=10)#Draw many red scatter points.
y2_values = [y*0.5 for y in y_values]
ax.scatter(x_values, y2_values, c=y2_values, cmap=plt.cm.Blues, s=10)
#Draw many blue scatter points, using colormap <Blues>.
ax.axis([0, 1100, 0, 1100000])#This specifies the range of each axis. x1x2y1y2

#Set chart title and lable axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick label
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')
#The second argument trims extra whitespace from the plot.
#Use the savefig function before the show function. Otherwise the saved file
#is blank.
plt.show()
