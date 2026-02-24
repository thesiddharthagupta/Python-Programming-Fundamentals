import os

os.makedirs("tables", exist_ok=True)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(rf"E:\Scratch.python\File_io_in_Python\tables\table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
