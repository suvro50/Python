import numpy as np
# Filtering = Refers to the process of selecting elements
#             from an array that match a given condition

# create people ages

ages=np.array([
    [21,17,19,20,16,30,18,65],
    [39,22,15,99,18,19,20,21]
])

# Filtering
teenagers=ages[ages < 18]
adults=ages[(ages >= 18) & (ages<65) ]
even_ages=ages[ages %2 ==0]
print(teenagers)
print(adults)
print(even_ages)

# V.V.I
#  np.where(condition, value_if_true, value_if_false)
new_adults=np.where(ages >=18 , ages, 0)
print("New Adults",new_adults)