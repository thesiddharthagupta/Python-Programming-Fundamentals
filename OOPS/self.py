class Employee:
    name = "Siddhu"
    language = "python"  #this is a class attribute
    salary = 12000000

    def getInfo(self):
        print(f"The name is {self.name}. The language is {self.language}. the salary is {self.salary}")

    def greet(self):
        print("Good Morning!")

Siddhu = Employee()
Siddhu.greet()
Siddhu.getInfo()  #or
Employee.getInfo(Siddhu)   # both works same 
