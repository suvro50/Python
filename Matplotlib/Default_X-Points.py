import matplotlib.pyplot as plt
import numpy as np

# If we do not specify the points on the x-axis, 
# they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
ypoints=np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints , marker="*") #marker= Mark each point with any symbol ,EXP: marker="*,&,+,_,|"

plt.show()