#fro the replace of the words from file
word = "programming python"   
with open(r"File_io_in_Python\replace.txt", "r") as f:
    content = f.read()

# replace both spellings just in case
contentNew = content.replace("programing python", "python")
contentNew = contentNew.replace("programming python", "python")

with open(r"File_io_in_Python\replace.txt", "w") as f:  # overwrite same file
    f.write(contentNew)