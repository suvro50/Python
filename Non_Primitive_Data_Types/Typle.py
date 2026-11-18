# Typle , It is faster than list
#  we can not insert and Remove any value here 
mark=(1,2,3,4,5,6,3,2,2,2)


print(mark,type(mark))

# find index , by given vlaue
print(mark.index(2))

# count how many time repet , which charactor
print(mark.count(2))

#Multipel touple
print("Multiple typle:")
con=(1,2,(2,3),('s','h','g'))
print(con)

print(con[2][1])  # print-> 3

#Touple hold list
print("Touple hold list:")
con=(1,2,[2,3],['s','h','g'])
print(con)

print(con[2][1])  # print-> 3

print(con[1])  # print-> 3


