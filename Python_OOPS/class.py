class person:
    name="Suvrojit"
    age=21
    position= "AI Engineer"

# Creating object
a=person()
print(a.name,"\n"+a.position)

# change name
a.name="Suvrojit bose"
print(a.name)


# pass by user

class student:
    university="United International University"
    def __init__(self,name,age):
        self.name=name
        self.age=age

# call class
s1=student("Suvro",21)
s2=student("Adi",18)
print(s1.name)
print(s1.university)
print(s2.age)