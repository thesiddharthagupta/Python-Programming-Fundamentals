with open("E:\\Scratch.python\\File_I-O_in_Python\\O\\test.txt", "r") as f:
    data = f.read()
    print(data)

num = data.split(",")   # Split into list of strings
count = 0               # Initialize counter

for val in num:         # Use 'num' instead of 'nums'
    if int(val) % 2 == 0:
        count += 1

print("Number of even values:", count)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #     else:
    #         num += data[i]
