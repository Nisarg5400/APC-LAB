# 1. Runtime polymorphism - Shape base class, area() overridden

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for s in shapes:
    print(f"{s.__class__.__name__} Area: {s.area()}")
