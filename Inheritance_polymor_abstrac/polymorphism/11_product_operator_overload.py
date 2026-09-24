# 11. Product class - overload == and > operators to compare price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Phone", 15000)
p2 = Product("Tablet", 15000)
p3 = Product("Laptop", 50000)

print("p1 == p2:", p1 == p2)
print("p3 > p1:", p3 > p1)
