def print_list(lst, idx=0):
    if idx == len(lst):      # Base case
        return
    
    print(lst[idx])         # Work
    print_list(lst, idx+1)  # Recursive call


fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits)
