"""4.Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total
price.
Solution: Create a class with functions add_item,remove_item,
and calculate_total."""

class ShoppingCart:
    def __init__(self):
        self.total = 0
        
    def add_item(self, price):
        self.total += price
        print(f"Added {price}rs worth, Cart Value:", self.total,"rs")

    def remove_item(self, price):
        self.total -= price
        print(f"Removed {price}rs worth, Cart Value:", self.total,"rs")

    def calculate_total(self):
        print("Total price:", self.total,"rs")


cart = ShoppingCart()

cart.add_item(100)
cart.add_item(200)
cart.remove_item(100)

cart.calculate_total()