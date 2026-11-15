# super() is used in a child class to call methods or the constructor of its parent class.



# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Calls Parent Constructor
        self.student_id = student_id

    def display(self):
        super().show()  # Calls Parent Method
        print("Student ID:", self.student_id)


# Object Creation
s1 = Student("Suvrojit", 21, "011231")
s1.display()