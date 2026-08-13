"""7. Design a Rectangle class with default attributes for length and width
set to 1. Include methods to set these attributes and calculate the area"""

class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle = Rectangle()

rectangle.set_length(10)
rectangle.set_width(5)

print("Area:", rectangle.calculate_area())