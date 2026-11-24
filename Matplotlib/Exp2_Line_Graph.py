import matplotlib.pyplot as plt

x=['Mon','Tues','Wed','Thur','Fri'] # x-axix
y=[10,15,7,20,12] # y-axix

plt.plot(x,y,linestyle="dashdot",marker="*",markersize="10",markerfacecolor="gold")

plt.title("Bakery Sales This Week") # Graph Title

plt.xlabel("Day of the week",fontsize="15")
plt.ylabel("Sales per day")

plt.show() # show the graph