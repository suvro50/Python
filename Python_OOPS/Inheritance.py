# Inheritance: It is an OOP concept where a child class acquires the attributes and methods of a parent class.


# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class
class Student(Person):

    def study(self):
        print(self.name, "is studying.")


# Creating Child Class Object
s1 = Student("Suvrojit", 21)

s1.display()  # Inherited from Person
s1.study()    # Defined inside Student





# Example-2

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class (inherits Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_student(self):
        print("Student ID:", self.student_id)


# Child Class (inherits Student)
class UniversityStudent(Student):
    def __init__(self, name, age, student_id, department):
        super().__init__(name, age, student_id)
        self.department = department

    def show_department(self):
        print("Department:", self.department)


# Creating Object
s1 = UniversityStudent("Suvrojit", 21, "011241", "CSE")

s1.show_person()      # From Person
s1.show_student()     # From Student
s1.show_department()  # From UniversityStudent