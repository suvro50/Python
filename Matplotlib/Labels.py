import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y,"o-g")


plt.title("Sports Watch Data" , color="blue", fontsize="20")
plt.xlabel("Average Pulse" , color="red", fontsize="18")
plt.ylabel("Calorie Burnage", color="y", fontsize="20")

plt.show()