'''
Program to keep reading numbers from the user and 
terminates when it computes sum of 5 even numbers
'''

sum = 0
count = 0
while True:
    x = int (input("Enter a number: "))
    if x % 2 != 0:
        continue
    else:
        sum += x
        count += 1
        if count ==5:
            break
print("sum = ", sum)



'''
input → check even?
         ❌ no → continue
         ✅ yes → add → count++
                   count==5? → break

'''
