# call autometicly when call function

class student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

   #Instance Method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        # Another fast way , called : f-strings
        print(f"Name is {self.name}\nAge is {self.age}")

s1=student("Suvrojit",21)
s1.display()