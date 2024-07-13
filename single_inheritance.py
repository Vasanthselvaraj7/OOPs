"""
#single inheritance

#Base Class
class book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def get_description(self):
        return f"Title { self.title} and Author is {self.author}"

#Derived Class

class textbook(book):
    def __init__(self,title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def get_description(self):
        return f"Title { self.title} and Author is {self.author} and subject is {self.subject}"

#object for base class
Book = book("Ethical Hacking with Python", "sanjib sinha")
print(Book.get_description())


#object for derived class
textbook = textbook("Harry Potter", "J.K.Rolling", "Magic")
print(textbook.get_description())
"""

"""
#base class

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_discription(self):
        return f"Year : {self.year}, make : {self.make}, Model : {self.model}"

#Derived Class
class Car(Vehicle):
    def __init__(self,make, model, year, doors ):
        super().__init__(make, model, year)
        self.doors = doors


    def get_description(self):
        return f"Year : {self.year}, make : {self.make}, Model : {self.model}, No.of.doors: {self.doors}"
if __name__ == "__main__":
    #object for Vehicle
    Vehicle = Vehicle("Chevrolet", "Camaro", 1967)
    print(Vehicle.get_discription())

    #object for car
    Car = Car("FORD", "endeavor", 2003, 5)
    print(Car.get_description())
"""


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"Year : {self.year}, make : {self.make}, Model : {self.model}"


# Derived Class
class Car(Vehicle):

    def get_description(self, doors):
        self.doors = doors
        return f"Year : {self.year}, make : {self.make}, Model : {self.model}, No.of.doors: {self.doors}"


if __name__ == "__main__":
    #object for Vehicle
    Vehicle = Vehicle("Chevrolet", "Camaro", 1967)
    print(Vehicle.get_description())

    #object for car
    Car = Car("FORD", "endeavor", 2003)
    print(Car.get_description(5))