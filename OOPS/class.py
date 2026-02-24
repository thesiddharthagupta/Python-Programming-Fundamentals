class employee:
    language = "python"  # this is a class attributes
    salary = 20000000

Siddharth = employee()
print(Siddharth.language , Siddharth.salary)

Uttam = employee()
Uttam.name = "Uttam"   #this is instence attributes
print(Uttam.name , Uttam.language , Uttam.salary)


# here name is instance attributes aand salary and language are class attributes as they directly belongs to class