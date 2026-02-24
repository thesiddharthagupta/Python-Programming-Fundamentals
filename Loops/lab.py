''' librarian assigns a code number to books. To generate a digital checksum for a code, 
write a program that finds the sum of all digits of the given book code
'''

Bcode = int(input("Enter book code: "))

total = 0
while Bcode > 0:
    digit = Bcode % 10  # to "get" last digits
    total += digit      # add digit
    Bcode //= 10         # to "Remove" last digit

print("Checksum (sum of digit) = ", total)


''''
code = input("Enter book code: ")

total = 0
for digit in code:
    total += int(digit)

print("Checksum =", total)

'''