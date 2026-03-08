
code = input("Enter book code: ")

total = 0
for digit in code:
    total += int(digit)

print("Checksum =", total)

