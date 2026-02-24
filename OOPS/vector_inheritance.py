class vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show (self):
        print(f"{self.x}i + {self.y}j")

class Vector3d(vector2d):
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.z = z
    def show (self):
        print(f"{self.x}i + {self.y}j + {self.z}k")

v = Vector3d(1,2,3)
v.show()
        
