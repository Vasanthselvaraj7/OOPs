#hybrid (two are more than inheritance)

class vehicle:
    def start(self):
        return "Engine start"

class car(vehicle):
    def drive(self):
        return "Drive the car"

class bike(vehicle):
    def ride(self):
        return "Ride the bike"

class electric_vehicle:
    def charge(self):
        return "Charge the vehicle"

class electric_car(car, electric_vehicle):
    def eco_mode(self):
        return "Drive in eco mode"

class electric_bike(bike, electric_car):
    def no_fuel(self):
        return "electric bike don't need fuel"

obj1 = electric_bike()
print(obj1.start())
print(obj1.eco_mode())
print(obj1.no_fuel())
print(obj1.charge())
print(obj1.drive())
print(obj1.ride())

