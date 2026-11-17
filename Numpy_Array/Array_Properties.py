import numpy as np

# ndim--> Number of dimensions
# shape--> Number of rows and columns
# size--> Total number of elements
# dtype--> Data type of elements

arr = np.array([
    [1,4,3],
    [2,4,5]
])
arr1 = np.array([
    [[1,4,3],[5,6,7]],
    [[2,4,5],[1,2,3]]
])


print("Dimensions: ",arr.ndim)
print("Shapes: ",arr.shape)
print("Total number of element:",arr.size)
print(arr.dtype)

print("Dimensions: ",arr1.ndim)
