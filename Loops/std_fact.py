n = int(input("Enter fact number: "))

fact = 1

for i in range (1, n+1):
    fact = fact*i
print("factorial is :", fact)