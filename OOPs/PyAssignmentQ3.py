"""3.Write a Python program to create a class representing a bank. Include
methods for managing customer accounts and transactions."""

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

    def show_balance(self):
        print("Customer:", self.name)
        print("Balance:", self.balance)


customer1 = Bank("Raj", 5000)

customer1.deposit(1000)
customer1.withdraw(500)
customer1.show_balance()