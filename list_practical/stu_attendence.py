students = ["Amit", "Rahul", "Nisarg", "Sahil"]

print("Total students:", len(students))

name = input("Search student: ")

if name in students:
    print("Student is present")
else:
    print("Student is absent")

students.append("Rohit")
students.remove("Sahil")

print("Updated list:", students)