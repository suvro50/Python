# All classes have a function called :Constructor: __init__(),
#__init__() is called automatically when an object is initialized.

class person:
    name="Suvrojit"
    age=21
    position="AI Engineer"

    # this function called autometicly when the object created
    def __init__(self):
        print(type(self))
        print("Hello bro , how are you")

a=person() # call class

a2=person()



# send values through object 
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=student("Hello Suvrojit",21)
print(a.name)
print(a.age)


