num = int(input("Enter a number: "))

temp = num              #save original number
power = len(str(num))   #count digit
total = 0               #start from 0

while temp > 0:         #repeat until the number become zero
    digit = temp % 10   #takes last digit
    total += digit ** power     # add digit^power
    temp //= 10     #to remove last digit
if total == num:
    print("Armstrong number")
else:
    print("Not a Armstrong number")