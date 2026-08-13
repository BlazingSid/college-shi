import math

"""2.Write a Python program to create a class representing a Circle. Include
methods to calculate its area and perimeter."""

class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        print(f"The Area of the Circle is:", {area})

    def calculate_perimeter(self):
        perimeter = math.pi  * (self.radius * 2)
        print(f"The Perimeter of the Circle is:", {perimeter})

circle1 = circle(23)
circle2 = circle(3)

circle1.calculate_area()
circle1.calculate_perimeter()
circle2.calculate_area()
circle2.calculate_perimeter()

