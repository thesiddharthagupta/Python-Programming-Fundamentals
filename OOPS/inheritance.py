class Employee:
    company = "ITC"
    def show(self):  #base class
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):     #derived or child class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is giid with {self.showLanguage}")

a = Employee()
b = Programmer()

print(a.company , b.company)