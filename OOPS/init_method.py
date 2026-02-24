class Employee:
    name = "Siddhu"
    language = "python"  #this is a class attribute
    salary = 12000000

    def __init__(self, name, salary, language):     #this is dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language


    def getInfo(self):
        print(f"The name is {self.name}. The language is {self.language}. the salary is {self.salary}")

    def greet(self):
        print("Good Morning!")

Siddhu = Employee("siddhu", 130000000, "javaScript")
Siddhu.greet()
# Siddhu.getInfo()  #or
Employee.getInfo(Siddhu)   # both works same 
