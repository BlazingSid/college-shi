class student:
    name = ""
    age = 0
    grade = ""
    total_marks = 0
    attendance = 0

student1 = student()
student1.name = "shahid"
student1.age = 18
student1.grade = "A"    
student1.total_marks = 450
student1.attendance = 90    

student2 = student()
student2.name = "pranav"
student2.age = 18   
student2.grade = "B"
student2.total_marks = 400
student2.attendance = 85
 
student3 = student()
student3.name = "sahil"    
student3.age = 18
student3.grade = "A"
student3.total_marks = 420
student3.attendance = 88

print(f"{student1.name} is {student1.age} years old, has grade {student1.grade}, scored {student1.total_marks} marks and has {student1.attendance}% attendance.")
print(f"{student2.name} is {student2.age} years old, has grade {student2.grade}, scored {student2.total_marks} marks and has {student2.attendance}% attendance.")
print(f"{student3.name} is {student3.age} years old, has grade {student3.grade}, scored {student3.total_marks} marks and has {student3.attendance}% attendance.")
