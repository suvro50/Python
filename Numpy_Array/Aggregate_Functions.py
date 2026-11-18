import numpy as np
# Aggregate Functions = summarize data and typically
#                        return the single value

arr=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])  # shapes: (2,5)

print(arr.shape)

print(np.sum(arr)) #sum
print("Max:",np.max(arr)) #max
print("Min:",np.min(arr)) #min
print("Max position:",np.argmax(arr)) # position of max
print("Min position:",np.argmin(arr)) # position of min

# sum all row 
print("Row sum:",np.sum(arr,axis=0))
# sum all column
print("Column sum:",np.sum(arr,axis=1))

print(np.mean(arr)) #average

# Low std: Values are close to the mean.
# High std: Values are spread far from the mean.
print(np.std(arr)) # Standard Deviation


# Low variance: Values are close to the mean.
# High variance: Values are spread far from the mean.
print(np.var(arr)) # Variance