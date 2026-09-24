# 6. Student base class, calculate_grade() overridden

class Student:
    def calculate_grade(self):
        pass


class EngineeringStudent(Student):
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        return "A" if self.marks >= 75 else "B"


class MedicalStudent(Student):
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        return "A" if self.marks >= 80 else "B"


class ManagementStudent(Student):
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        return "A" if self.marks >= 70 else "B"


students = [EngineeringStudent(78), MedicalStudent(85), ManagementStudent(72)]
for s in students:
    print(f"{s.__class__.__name__} Grade: {s.calculate_grade()}")
