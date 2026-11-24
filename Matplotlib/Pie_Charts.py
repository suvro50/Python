import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

# As you can see the pie chart draws one piece (called a wedge) 
# for each value in the array (in this case [35, 25, 25, 15]).
#By default the plotting of the,
#                first wedge starts from the x-axis and moves counterclockwise:
plt.pie(y)
plt.show() 