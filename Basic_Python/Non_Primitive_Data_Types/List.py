#List
# In list different data type also allow
mark=[1,2,3,"Suvro",5,6]
print(mark)

# Add value at he end
mark.append(40)
print(mark)

# Add value at the beginning or any position
# insert(position,value)
mark.insert(0,5)
print(mark)

print(type(mark))
print(mark)

# print index
print(mark[1])
# last first index
print("last index vale:",mark[-1])

# length
print("length:")
print(len(mark))

# sublist : list[start:end]

# print(mark[0:4])
print("Reverse:",mark[-3:-1])



# Add multiple values at the last
mark.extend([100,200,300])
print(mark)

# check exist or not 
print(100 in mark)
print(500 in mark)

# Clear full list
mark.clear()
print(mark)