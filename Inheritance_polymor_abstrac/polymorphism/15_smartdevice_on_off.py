# 15. SmartDevice base class, turn_on() and turn_off() overridden

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan turned on")

    def turn_off(self):
        print("Fan turned off")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned on")

    def turn_off(self):
        print("AC turned off")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")


devices = [Light(), Fan(), AC(), TV()]
for d in devices:
    d.turn_on()
    d.turn_off()
