# NumPy is one of the most powerful and important Python libraries, especially for numerical computing.
# Numerical means anything related to numbers and mathematical calculations.
# Array is the fundamantal object in Numpy

# For install Numpy : pip install numpy
import numpy as np

arr = np.array([1,2,3,4,5]) # numpy array

print(type(arr))
print(arr)

print(arr+2)

# 2D Array
arr2=np.array( [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
)

print(arr2)

# 3D array
arr3=np.array([
    [ [1,2],[3,4] ],
    [ [5,6],[7,8] ]
])
print(arr3)