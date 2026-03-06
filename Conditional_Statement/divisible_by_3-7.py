'''Write a program to check whether a number is divisible by 3 and 7'''

spam = int(input("Enter the number: "))
if (spam % 3 == 0) and (spam % 7 ==  0):
    print("can be divisible by 3 and 7: ", spam)
else:
    print( spam, ": cannt by disible by 3 and 7")
