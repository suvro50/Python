import numpy as np

# Creates a random number generator.
# It is the recommended modern approach for generating random numbers in NumPy.
rng=np.random.default_rng()

print(rng.integers(low=1, high=10)) # also set limit
print(rng.integers(low=1, high=10, size=3)) # also set size

# Reproduce the same result again and again 
rng1=np.random.default_rng(seed=1)
print(rng1.integers(low=1, high=10))

# Floteing numbers
# if want same value = np.random.seed(seed=1)
print("Uniform: ",np.random.uniform(low=1 , high=10, size=(3,2) ) )

# Random fruits selection
# fruits image = Win + ;

fruits=np.array(["apple🍎","orange🍊","banana🍌","coconut🥥","pineapple🍍"])

fruits=rng.choice(fruits, size=3)
print(fruits)