#factorial 

def factorial(n):  #function defination
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(5)  #function call