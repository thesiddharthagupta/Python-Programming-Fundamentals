"""

lst = [1,2,3,3,2,1]

copy_list = lst.copy()
copy_list.reverse()

if copy_list == lst:
    print("This is palindrome")
else:
    print("This is not palindrome")



""" #<= this is also a method

lst = [1,2,3,3,2,1]

if lst == lst[::-1]:
    print("This is palindrome")
else:
    print("This is not palindrome")
