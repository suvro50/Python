import matplotlib.pyplot as plt
import numpy as np
# V.V.I:
# plt.subplot(rows, columns, index), here index start from 1 not 0
# here index is very importent
# Rows and columns directly control the arrangement and layout of your graphs.
#For a single subplot layout, keep the number of rows and columns the same;
# only change the index for each graph.


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,2)
plt.plot(x,y)


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.show()