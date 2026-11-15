# Encapsulation: Keeping data and methods inside a class, hiding sensitive data, and controlling how that data is accessed or modified.


class BankAccount:

    def __init__(self, name, balance):
        self.name = name              # Public
        self.__balance = balance     # Private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")


account = BankAccount("Suvrojit", 5000)

print("Name:", account.name)
print("Balance:", account.get_balance())

account.deposit(1000)

print("Updated Balance:", account.get_balance())