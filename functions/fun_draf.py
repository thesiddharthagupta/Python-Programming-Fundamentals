def greater():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if a > b and a > c:
        print(f"{a} is Greater Number")

    if b > c and b > a:
        print(f"{b} is Greater Number")

    if c > b and c > a:
        print(f"{c} is Greater Number")

greater()
    