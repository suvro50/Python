
import numpy as np
arr = np.array([
    [[1,4,3],[5,6,7]],
    [[12,13,14],[16,8,3]],
    [[5,6,7],[8,50,10]]
])

print(arr[0,0,0]) # 1
print(arr[1,0,2]) #14
print(arr[2,1,1])  #50


# Add numbers -> 1+12+5 = 18 
add=arr[0,0,0]+ arr[1,0,0] + arr[2,0,0]
print("After add:",add)