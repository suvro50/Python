
# public-> Use when the variable can be accessed and modified from anywhere.
# protected-> Use when the variable is intended for internal use within a class and its subclasses.
# private-> Can not access it directly using its original name from outside the class or from a subclass.

# Symbols: 
# Public: name ,  protected: _name , private: __name



class Student:

    def __init__(self, name, department, password):
        self.name = name              # Public
        self._department = department # Protected
        self.__password = password    # Private

    def show_details(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Password:", self.__password)

# Inheritance
class Result(Student):

    def show_result(self):
        print("Student:", self.name) 
        print("Department:", self._department)
        # print(self.__password)  # Error


s = Result("Suvrojit", "CSE", "abc123")

s.show_details()
s.show_result()