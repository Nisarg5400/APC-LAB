# 5. Multilevel inheritance - Person -> Student -> ResearchStudent

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display(self):
        super().display()
        print(f"Roll No: {self.roll_no}, Course: {self.course}")


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}, Guide: {self.guide_name}")


r1 = ResearchStudent("Sam", 24, 501, "M.Tech", "AI in Healthcare", "Dr. Sharma")
r1.display()
