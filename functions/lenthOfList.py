num = [1, 5, 9, 7, 6, 2, 0]
fruits = ["apple", "orange", "grapes", "banana", "pineapple"]

def print_len(lst):
    print(len(lst))

def print_list(lst):
    for item in lst:
        print(item, end=" ")

print_list(fruits)
print()          # for new line
print_len(num)
