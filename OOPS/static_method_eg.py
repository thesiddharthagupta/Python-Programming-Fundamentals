class animals:
    def eat(self):
        print("Animal is eating")


class pets(animals):
    pass


class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")


# create object
d = dog()

d.eat()   # from animals
d.bark()  # from dog
