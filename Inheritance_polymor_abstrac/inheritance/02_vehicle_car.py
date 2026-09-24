class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        super().display()
        print(f"Fuel Type: {self.fuel_type}, Price: {self.price}")

    def discounted_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


c1 = Car("Maruti", "Swift", "Petrol", 700000)
c1.display()
print("Discounted Price:", c1.discounted_price(10))
