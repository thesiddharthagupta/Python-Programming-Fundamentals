'''Write a function to find the largest element in a list.'''

def find_largest(lst):
    largest = lst[0]          # Step 1: assume first element is the largest

    for num in lst:           # Step 2: go through each element
        if num > largest:     # Step 3: compare
            largest = num     # Step 4: update if bigger found

    return largest            # Step 5: return the result



