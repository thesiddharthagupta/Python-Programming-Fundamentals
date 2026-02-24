lst = [10, 20, 30, 40, 50]

element = int(input("Enter element to search: "))       

found = False

for item in lst:
    if item == element:
        found = True
        break

if found:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")
