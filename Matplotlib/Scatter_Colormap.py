import matplotlib.pyplot as plt
import numpy as np
#Colormap (cmap): A predefined color scheme used to automatically
# assign colors to data points based on their numerical values.

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# numerical values for color
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='rainbow') # exp:cmap='rainbow',cmap='coolwarm',cmap='inferno'
plt.colorbar()
plt.show()
