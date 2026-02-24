f = open("E:\Scratch.python\File_io_in_Python\poem.txt", "r")
content = f.read()
if ("twinkle" in content):
    print("the word Twinkle is present in the content")
else:
    print("not present in the content")
f.close()
