# Sine and Cosine generating

from matplotlib import pyplot as plt # Importing module
import numpy as np

x_axis = np.arange(0, 4*np.pi, 0.1) # Start, stop, step
y_sine = np.sin(x_axis)
y_cosine = np.cos(x_axis)

plt.plot(x_axis, y_sine) # Sine curve
plt.plot(x_axis, y_cosine) # Cosine curve
plt.show()

degree = '\u00B0'


