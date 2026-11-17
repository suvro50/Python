import numpy as np

arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# arr[start:end:step]  -> ending index is exclusive
print(arr[0:3])
print(arr[0:4]) # print all , because take extra index
# another way to print all--> print(arr[0:])