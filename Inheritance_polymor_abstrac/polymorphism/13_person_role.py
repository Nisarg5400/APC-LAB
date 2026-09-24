# 13. Person base class, display_role() overridden, list + loop

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("I am a Student")


class Faculty(Person):
    def display_role(self):
        print("I am a Faculty member")


class Administrator(Person):
    def display_role(self):
        print("I am an Administrator")


people = [Student(), Faculty(), Administrator()]
for p in people:
    p.display_role()
