#Class Method: Used to access or change class variables without creating an object.


# V.V.I @classmethod changes class-level variables.
class student:
    name="suvrojit"
    age=21

    @classmethod
    def change_name(cls,newname):
        cls.name=newname
       

    def display(self):
        print(f"Name is {self.name}\nAge is {self.age}")


s=student()

s.display()
s.change_name("Dip")
s.display()