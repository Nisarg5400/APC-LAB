# 10. Student class - overload > and < operators to compare marks

class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks


s1 = Student("Amit", 450)
s2 = Student("Priya", 470)

if s1 > s2:
    print(f"{s1.name} scored more")
elif s1 < s2:
    print(f"{s2.name} scored more")
else:
    print("Both scored equal")
