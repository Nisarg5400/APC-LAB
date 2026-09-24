# 15. Hierarchical inheritance - Animal -> Dog, Cat, Cow

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")


class Cow(Animal):
    def sound(self):
        print(f"{self.name} says Moo!")


animals = [Dog("Rex"), Cat("Whiskers"), Cow("Bella")]
for a in animals:
    a.eat()
    a.sound()
