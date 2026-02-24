with open(r"e:\Scratch.python\File_io_in_Python\test.txt", "r") as source:
    with open(r"e:\Scratch.python\File_io_in_Python\copy.txt", "w") as destination:
        for line in source:
            destination.write(line)

print("File copied successfully!")
