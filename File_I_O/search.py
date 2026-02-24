with open (r"File_io_in_Python\replace.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("yes, python is present in text")
else:
    print("No, Python is not present in text")


with open(r"File_io_in_Python\replace.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        if "python" in line.lower():
            print("Python found at line:", i)
