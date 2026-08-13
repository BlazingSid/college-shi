"""Calculating Student Results: Develop a class to accept a student's
name and marks in three subjects, then calculate and display the total and
average marks"""

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_total(self):
        return self.mark1 + self.mark2 + self.mark3

    def calculate_average(self):
        return self.calculate_total() / 3

    def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", self.calculate_average())


student = Student("Shahid", 80, 75, 90)

student.display()