# All classes have a function called __init__(),
# Which is always executed when the class in being initiated

class person:
    name="Suvrojit"
    age=21
    position="AI Engineer"

    # this function called autometicly when the object created
    def __init__(self):
        print(type(self))
        print("Hello bro , how are you")

a=person()



# send values through object 
class student:
    def __init__(self,fullname,age):
        self.name=fullname
        self.age=age

a=student("Hello Suvrojit",21)
print(a.name)
print(a.age)


