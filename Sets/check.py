collection = {1, 2, 4, 8, 12, 25, 36, 14, 0}
a = int(input("Enter a number: "))
               
if a in collection:         # Check if 'a' is in the set
    print(f"{a} is present in the set")
else:
    print(f"{a} is NOT present in the set")

print("The set is:", collection)

