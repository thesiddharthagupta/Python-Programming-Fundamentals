class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Siddhu")
print(s1.name)
try:
    del s1.name
    print(s1.name)

except:
    print("Student' object has no attribute 'name'")
