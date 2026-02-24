try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as V:
    print("Value Error!")
except Exception as e:
    print(e)

print("Thank You!")