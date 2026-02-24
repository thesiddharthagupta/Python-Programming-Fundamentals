word = "learning"
with open("E:\Scratch.python\File_I-O_in_Python\O\practice.txt","r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("not found")
