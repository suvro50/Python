import matplotlib.pyplot as plt
import numpy as np

# A graph that uses individual dots to show the relationship, patterns, trends,
# and outliers between two variables (X and Y).
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6]) #The X-axis shows how old the car is.
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86]) # The Y-axis shows the speed of the car when it passes.


plt.scatter(x,y, color="r")
plt.show()