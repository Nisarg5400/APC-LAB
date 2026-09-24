# 10. Hybrid inheritance - Vehicle -> Car -> SportsCar, Vehicle -> Bike -> ElectricBike

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


class SportsCar(Car):
    def __init__(self, brand, doors, top_speed):
        super().__init__(brand, doors)
        self.top_speed = top_speed

    def display(self):
        super().display()
        print(f"Doors: {self.doors}, Top Speed: {self.top_speed}")


class Bike(Vehicle):
    def __init__(self, brand, wheels=2):
        super().__init__(brand)
        self.wheels = wheels


class ElectricBike(Bike):
    def __init__(self, brand, battery_range):
        super().__init__(brand)
        self.battery_range = battery_range

    def display(self):
        super().display()
        print(f"Wheels: {self.wheels}, Battery Range: {self.battery_range} km")


sc = SportsCar("Ferrari", 2, 300)
eb = ElectricBike("Ather", 100)
sc.display()
eb.display()
