n = int(input("Enter number of days: "))

total = 0

for i in range(n):
    sale = float(input("Enter sale: "))
    total = total + sale

print("Total sales =", total)
