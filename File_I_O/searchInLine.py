with open(r"File_io_in_Python\replace.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        if "python" in line.lower():
            print("Python found at line:", i)
