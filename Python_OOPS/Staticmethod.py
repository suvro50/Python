# Staticmethod that belongs to a class but does not receive self or cls automatically.
#  It can be called without creating an object.
# @staticmethod does not receive self or cls automatically.
class Math:

    @staticmethod
    def add(a,b):
        print(a+b)

Math.add(2,2)


# Example-2
class Number:

    @staticmethod
    def check(num):
        if num % 2 ==0:
            print("EVEN")
        else:
            print("ODD")
a=Number()
a.check(10)
a.check(3)