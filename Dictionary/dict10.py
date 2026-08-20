student_marks = {}
for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks of {name}: "))
    student_marks[name] = mark
print("Student marks dictionary:", student_marks)