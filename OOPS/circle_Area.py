class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print("Area is :", c1.area())
print("Perimeter is :", c1.perimeter())