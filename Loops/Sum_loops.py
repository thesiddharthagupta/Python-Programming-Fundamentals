''' Print the sum of first 10 natural numbers.'''


# # Ask the user how many natural numbers to sum
# n = int(input("Enter how many natural numbers to add: "))

# # Calculate the sum using range and sum()
# total = sum(range(1, n + 1))

# print("The sum of first", n, "natural numbers is:", total)




# by while loop:
n = int(input("Enter natural number: "))  #ask the user how many number to sum
i = 1
total = 0
while(i<n):
    i += 1
    total += i # adding in total  "total = total + i"

    print("the sum of natural number is: ", total)

