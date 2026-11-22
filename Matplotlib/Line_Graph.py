# Matplotlib → A Python library used for creating data visualizations, such as line graphs,
# bar charts, pie charts, and histograms, to understand and analyze data easily.

# install -->  pip install matplotlib
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]

# plot() → Used to create a line graph by plotting data points on the X-axis and Y-axis.

plt.plot(x,y)  # Creates a graph
plt.show()  # Displays the graph

# Example-2

x1=['Mon','Tues','Wed','Thur','Fri'] # x-axix
y1=[10,15,7,20,12] # y-axix

plt.plot(x1,y1)
plt.title("Bakery Sales This Week") # Graph Title

plt.xlabel("Day of the week")
plt.ylabel("Sales per day")

plt.show()