#hierarchical inheritance(multiple classes inherit from base class)

class car:
    def door(self,number):
        self.number = number
        return f"normal cars have{self.number} doors"

class wheels(car):
    def wheel(self,wheels_number):
        self.wheels_number = wheels_number
        return f"most probably cars have only {self.wheels_number} wheels"

class speed(car):
    def fast(self,speed):
        self.speed = speed
        return f"Cars usually faster than bycycle"

obj1 = wheels()
obj2 = speed()

print(obj1.wheel(4))
print(obj2.fast(250))

print(obj1.door(4))
print(obj2.door(4))


