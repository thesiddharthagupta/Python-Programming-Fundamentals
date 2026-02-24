class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square is {self.n * self.n}")

    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")

    def SquareRoot(self):
        print(f"the Square Root is {self.n ** 1/2}")

    def Add(self):
        print(f"the Add is {self.n + self.n}")

    def Subtract(self):
        print(f"the Subtract is {self.n - self.n}")

a = calculator(int(input("Enter a number: ")))
a.square()
a.cube()
a.Add()
a.Subtract()
a.SquareRoot()