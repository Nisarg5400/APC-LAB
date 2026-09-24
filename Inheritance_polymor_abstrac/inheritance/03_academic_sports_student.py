class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return self.marks + self.sports_points

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Sports Points: {self.sports_points}")
        print("Overall Performance:", self.overall_performance(),"out of 120 .")


s1 = Student("Amit", 85, 20)
s1.display()
