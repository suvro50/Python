import matplotlib.pyplot as plt
import numpy as np

# Add labels to the pie chart with the labels parameter.
x=np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

mycolors = ["black", "hotpink", "b", "#4CAF50"] # Add extra color

# V.V.I:
# with explode function->Pull the "Apples" wedge 0.2 
# and "Bananas" wedge 0.3 from the center of the pie:
plt.pie(x,labels=mylabels ,startangle = 60 , explode=[0.2,0.3,0,0], colors=mycolors)

plt.title("My Pie Charts")
plt.legend() # To add a list of explanation for each wedge, use the legend() function
plt.show()