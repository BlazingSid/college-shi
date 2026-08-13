"""1. Car Class: Create a Car class with attributes make, model, and year.
Include a method to display the details of the car."""

class car:
    def __init__(self, Brand, Model, Year):
        self.brand = Brand
        self.model = Model
        self.year = Year

    def display_details(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

car1 = car("Toyota", "Camry", 2024)
car2 = car("Hyundai", "Creta", 2016)
car3 = car("Kia", "Seltos", 2021)

car1.display_details()
car2.display_details()
car3.display_details()


