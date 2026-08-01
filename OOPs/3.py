class student:
    no = 0
    name = ""
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0


max_marks = 400

student1 = student()
student1.no = 1
student1.name = "shahid"
student1.s1 = 80
student1.s2 = 90
student1.s3 = 70
student1.s4 = 60
total_marks1 = student1.s1 + student1.s2 + student1.s3 + student1.s4

student2 = student()
student2.no = 2
student2.name = "anu"
student2.s1 = 90
student2.s2 = 80
student2.s3 = 70
student2.s4 = 60
total_marks2 = student2.s1 + student2.s2 + student2.s3 + student2.s4

student3 = student()
student3.no = 3
student3.name = "ayush"
student3.s1 = 70
student3.s2 = 80
student3.s3 = 90
student3.s4 = 60
total_marks3 = student3.s1 + student3.s2 + student3.s3 + student3.s4

# printing
print(f"{student1.name} with {student1.no} has {(total_marks1 / max_marks) * 100}%")
print(f"{student2.name} with {student2.no} has {(total_marks2 / max_marks) * 100}%")
print(f"{student3.name} with {student3.no} has {(total_marks3 / max_marks) * 100}%")
