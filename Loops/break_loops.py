
spam = 25
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0    # initialization

while i < len(tup):
    if tup[i] == spam:
        print("Found an Index at:", i)
        break 
    else:
        print("Didnt Found")  
    i += 1
print("End of Loops at index :", i)