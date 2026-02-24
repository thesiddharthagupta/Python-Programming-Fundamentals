class Employee:
    a = 1

    @classmethod    #runs only on class attribute!
    def show(cls):
        print(f"The class attributes is {cls.a}")


e = Employee()
e.a = 45

e.show()