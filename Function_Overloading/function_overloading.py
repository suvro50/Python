# Python does not support function overloading. When we define multiple functions with the same name.

def add(a, b):
    print(a + b)

def add(a, b, c):
    print(a + b + c)

def add(a, b, c, d):
    print(a + b + c +d)

# if i create method with same name , than it keep's only the last one
# add(10,20)  # gives error
#add(10,20,20) # gives error
add(10,10,10,10)
