# 3. Vehicle base class, start() overridden

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key/button")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick/self-start")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with an ignition switch")


vehicles = [Car(), Bike(), Bus()]
for v in vehicles:
    v.start()
