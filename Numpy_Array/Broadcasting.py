# Broadcasting: NumPy automatically adjusts compatible array shapes to perform arithmetic operations without manually repeating elements.

# it marge small array to make larger array
# numpy can do operation's in different dimentin array, which one normaly not possible

import numpy as np

# make 2->  2D array
arr1=np.array([[1,2,3,4]]) # shape: (1,4)
arr2=np.array([[1],[2],[3],[4]])  # shape:(4,1)

print(arr1.shape)
print(arr2.shape)

# Broadcasing 
print(arr1+arr2)
print(arr1*arr2)

# shapes must be complete compatible.


arr3=np.array([1,2,3,4]) # shapes: (4,)
arr4=np.array([2,3,4]) # shapes: (3,)
print(arr3.shape)
print(arr4.shape)

#ERROR
#print(arr3*arr4)

arr5=np.array([[1,2],[2,3]]) # shapes: (2,2)
arr6=np.array([[1,2]]) # shapes:(1,2)
print(arr5.shape)
print(arr6.shape)
# shape metch with (2,2) and (1,2)
print(arr5+arr6) 


# If both dimensions are the same, or either one is 1, broadcasting works. 
# Otherwise, it gives a Broadcasting Error.
# Compare	Result
# 4 vs 4	Allowed
# 3 vs 1	Allowed
# 1 vs 5	Allowed
# 3 vs 2	Error
# 4 vs 5	Error