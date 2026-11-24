# A histogram is a graph showing frequency distributions.
import matplotlib.pyplot as plt
import numpy as np

# This will generate a random result, and could look like this:
x= np.random.normal(170,10,250)

print(x)

# The hist() function will read the array and produce a histogram:
plt.hist(x)
plt.title('Bar Graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()