from matplotlib import pyplot as plt

#plt.style.use('fivethirtyeight') # Adding style
plt.xkcd() # Adding comics style
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] # X axis

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] # Y curve

plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs') # Add axis and curve to the diagram
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='#5a7d9a', marker='o', label='Python') # Add axis and curve to the diagram

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#adad3b', label='JavaScript') # Add axis and curve to the diagram

plt.xlabel('Ages') # Label for X axis
plt.ylabel('Median Salary (USD)') # Label for Y axis
plt.title('Median Salary (USD) by Age') # Title

#plt.legend(['All Devs', 'Python']) # Legend for curves, it has to be in right order with arguments added to plot
plt.legend() # Without arguments because in plot method it is already label argument
plt.grid(True) # Adding the grid
plt.tight_layout() # padding
plt.savefig('first.png') # Saving as a png file
plt.show() # Show diagram
