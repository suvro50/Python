import numpy as np

# comparison operators return the boolean value

scores=np.array([91,55,100,73,82,64])

# if comparison metch than return ->True else false

print(scores == 100) 
print(scores >= 60)
print(scores < 60)

# make: false =0
scores[scores < 60 ] = 0
print(scores)