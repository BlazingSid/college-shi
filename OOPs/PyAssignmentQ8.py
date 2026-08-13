"""8. Object Count Tracker: Design a class that tracks how many objects
have been created from it and has a method to display this count"""

class Object:
    count = 0

    def __init__(self):
        Object.count += 1

    def display_count(self):
        print("Number of objects:", Object.count)


obj1 = Object()
obj2 = Object()
obj3 = Object()

obj3.display_count()