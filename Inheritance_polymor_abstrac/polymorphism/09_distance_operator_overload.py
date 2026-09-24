# 9. Distance class - overload + operator, normalize feet/inches

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = (self.inches + other.inches)
        total_feet = self.feet + other.feet + total_inches // 12
        total_inches = total_inches % 12
        return Distance(total_feet, total_inches)

    def display(self):
        print(f"{self.feet} feet {self.inches} inches")


d1 = Distance(5, 8)
d2 = Distance(3, 7)
d3 = d1 + d2
d3.display()
