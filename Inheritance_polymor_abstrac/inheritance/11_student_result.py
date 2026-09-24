# 11. Single inheritance - Student -> Result

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks   # list of 3 subject marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        percent = self.percentage()
        if percent >= 75:
            return "A"
        elif percent >= 60:
            return "B"
        else:
            return "C"


r1 = Result(101, "Amit", "B.Tech", [85, 90, 78])
print(f"Name: {r1.name}, Total: {r1.total()}, Percentage: {r1.percentage():.2f}, Grade: {r1.grade()}")
