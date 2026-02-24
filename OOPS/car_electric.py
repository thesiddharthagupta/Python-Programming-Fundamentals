# Parent class
class Car:
    def __init__(self, make, colour):
        self.make = make
        self.colour = colour


# Child class 1
class ElectricCar(Car):
    def __init__(self, make, colour, price, range_km):
        super().__init__(make, colour)
        self.price = price
        self.range = range_km

    def display(self):
        print("Electric Car")
        print(self.make, self.colour, self.price, self.range)


# Child class 2
class PetrolCar(Car):
    def __init__(self, make, colour, price, range_km):
        super().__init__(make, colour)
        self.price = price
        self.range = range_km

    def display(self):
        print("Petrol Car")
        print(self.make, self.colour, self.price, self.range)


# ----- Main -----

e = ElectricCar("Tesla", "White", 5000000, 400)
p = PetrolCar("Honda", "Black", 1500000, 600)

e.display()
p.display()
