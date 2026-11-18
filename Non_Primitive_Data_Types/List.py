#List -> Mutable
# In list different data type also allow
mark=[1,2,3,"Suvro",5,6]
print(mark)

# Add value at he end use->append
mark.append(40)
print(mark)

# Add value at the beginning or any position
# insert(position,value)
mark.insert(0,5)
print(mark)

# update list use -> mark[0]=5
# Delete value index whise-> mark.pop(2)
# Delete data value whise-> mark.remove(6)
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

# one list can store multiple list
print("Multiple list:")

contain=[1,2,[1,2,3],['a','s','s'],[2.3,5.6]]
print(contain)

print(contain[2][0]) # print: 1
print(contain[3][1])  # print: s

# slicing
print("slicing:")
arr=[1,2,3,4,5]
temp=arr[2:]
print(arr[2:])

# print all pair number from a list
ls=[1,2,3,4,5]

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        print(ls[i],ls[j])
