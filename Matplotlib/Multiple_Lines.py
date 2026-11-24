import matplotlib.pyplot as plt
import numpy as np


x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])

# Multiple lines
plt.plot(x,linewidth="10")
plt.plot(y)
plt.show()

# I can also plot many lines by adding the points for 
# the x- and y-axis for each line in the same plt.plot() function.