class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class manager(Programmer):
    def __init__(self):
       super().__init__()
       print("Constructor of manager")
    c = 3

x = manager()
print(x.a, x.b, x.c)