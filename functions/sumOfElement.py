'''Write a function to return the sum of elements in a list.'''
def sum_list(lst):
    total = 0
    for item in lst:
        total = total + item
    return total
number = [1,2,3,4]
answer = sum_list(number)
print("Sum is:",answer)
