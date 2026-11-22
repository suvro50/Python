import matplotlib.pyplot as plt

x1=['Mon','Tues','Wed','Thur','Fri'] # x-axix
y1=[10,15,7,20,12] # y-axix

plt.plot(x1,y1)
plt.title("Bakery Sales This Week") # Graph Title

plt.xlabel("Day of the week")
plt.ylabel("Sales per day")

plt.show() # show the graph