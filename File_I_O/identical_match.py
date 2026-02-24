# Program to check if two files are identical

with open("file1.txt", "r") as f1:
    with open("file2.txt", "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

        if content1 == content2:
            print("Both files are identical.")
        else:
            print("Both files are different.")
