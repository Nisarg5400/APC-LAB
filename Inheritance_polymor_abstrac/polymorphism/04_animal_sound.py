# 4. Animal base class, sound() overridden

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


class Lion(Animal):
    def sound(self):
        print("Lion roars")


animals = [Dog(), Cat(), Cow(), Lion()]
for a in animals:
    a.sound()
