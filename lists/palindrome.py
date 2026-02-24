lst = [1,2,3,3,2,1]

copy_list = lst.copy()
copy_list.reverse()     #reverse keyword for reverse

if copy_list == lst:
    print("This is Palindrome")
else:
    print("This is not Palindrome")