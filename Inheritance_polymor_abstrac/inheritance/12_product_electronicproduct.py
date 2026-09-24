# 12. Single inheritance - Product -> ElectronicProduct

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


p1 = ElectronicProduct(1, "Laptop", 50000, "Dell", "2 years")
print(f"Product: {p1.name}, Brand: {p1.brand}, Warranty: {p1.warranty}")
print("Final Price after 10% discount:", p1.final_price(10))
