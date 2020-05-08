# Sine and Cosine generating

from matplotlib import pyplot as plt # Importing module
import numpy as np

x_axis = np.arange(-4*np.pi, 4*np.pi, 0.1) # Start, stop, step
x_axis_visible = ['-4\u03A0', '-2\u03A0', '0', '2\u03A0', '4\u03A0'] 
y_sine = np.sin(x_axis)
y_cosine = np.cos(x_axis)

plt.style.use('fivethirtyeight')

plt.plot(x_axis, y_sine, color='#444444', label='sinus x') # Sine curve
plt.plot(x_axis, y_cosine, color='#adad3b', label='cosinus x') # Cosine curve
plt.xticks(np.arange(-4*np.pi, 4*np.pi, 2*np.pi), labels=x_axis_visible)
plt.legend()
plt.tight_layout()
plt.savefig('sine.png')
plt.show()
degree = '\u00B0'


