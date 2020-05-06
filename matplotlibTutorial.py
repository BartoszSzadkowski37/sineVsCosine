from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight') # Adding style
#plt.xkcd() # Adding comics style
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] # X axis

x_indexes = np.arange(len(ages_x))

width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] # Y curve

plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs') # Add axises to the diagram

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width=width, color='#5a7d9a', label='Python') # Add axises  to the diagram

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes + width, js_dev_y, width=width, color='#adad3b', label='JavaScript') # Add axises to the diagram

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.xlabel('Ages') # Label for X axis
plt.ylabel('Median Salary (USD)') # Label for Y axis
plt.title('Median Salary (USD) by Age') # Title

#plt.legend(['All Devs', 'Python']) # Legend for curves, it has to be in right order with arguments added to plot
plt.legend() # Without arguments because in plot method it is already label argument
plt.grid(True) # Adding the grid
plt.tight_layout() # padding
plt.savefig('first.png') # Saving as a png file
plt.show() # Show diagram
