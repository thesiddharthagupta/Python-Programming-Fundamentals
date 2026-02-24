'''Write a function to return the maximum of two numbers'''
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
def maximum_num(a,b):
    if a>b:
        print("the maximum of two number are: ", a)
    else:
        print("the maximum of two number are: ", b)
    return a>b

maximum_num(a,b)
        
    