# 14. Multiple inheritance - Camera + Phone -> Smartphone

class Camera:
    def take_photo(self):
        print("Taking a photograph...")


class Phone:
    def make_call(self, number):
        print(f"Calling {number}...")


class Smartphone(Camera, Phone):
    def __init__(self, brand):
        self.brand = brand


s1 = Smartphone("Samsung")
s1.take_photo()
s1.make_call("9876543210")
