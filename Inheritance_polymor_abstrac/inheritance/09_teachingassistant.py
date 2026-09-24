# 9. Multiple + hierarchical inheritance - Person -> Student, Faculty -> TeachingAssistant

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, dept):
        Person.__init__(self, name)
        self.dept = dept


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll_no, dept):
        Student.__init__(self, name, roll_no)
        Faculty.__init__(self, name, dept)

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Department: {self.dept}")


ta = TeachingAssistant("Neha", 601, "Computer Science")
ta.display()
