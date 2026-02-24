class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Siddhu", 24000000, 24016 )
print(f"name : {p.name}\nsalary: {p.salary}\npin {p.pin}\ncompany: {p.company} ")

r = programmer("Rahul", 24000000, 24016 )
print(f"name : {r.name}\nsalary: {r.salary}\npin {r.pin}\ncompany: {r.company} ")