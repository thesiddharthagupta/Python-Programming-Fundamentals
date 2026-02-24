class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# instance creation should be outside the class
e = Employee()
e.a = 45

e.name = "Sidd gupta"
print(e.fname, e.lname)   #  e.name will print 
e.show()                  # The class attribute of a is 1