'''Write a function to print all elements of a list.'''

l = [1, 9, 7, "alish", "tom", "bob"]

def print_list(lst):
    for item in lst:
        print(item)

print_list(l)

    
"""

with range:

l = [1, 9, 7, "alish", "tom", "bob"]

def print_list(lst):
    for i in range(len(lst)):   # i = 0,1,2,3,4,5
        print(lst[i])           # print element at index i

print_list(l)


"""