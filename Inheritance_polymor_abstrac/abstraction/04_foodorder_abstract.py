# 4. Abstract class FoodOrder with calculate_bill() and delivery_charge()

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def delivery_charge(self):
        return 0   # dine-in / pickup, no delivery charge

    def calculate_bill(self):
        return self.amount + self.delivery_charge()


class HomeDeliveryOrder(FoodOrder):
    def delivery_charge(self):
        return 50

    def calculate_bill(self):
        return self.amount + self.delivery_charge()


r1 = RestaurantOrder(500)
h1 = HomeDeliveryOrder(500)

print("Restaurant Order Bill:", r1.calculate_bill())
print("Home Delivery Order Bill:", h1.calculate_bill())
