def reverse_string(s):
    return s[::-1]

spam = input("ENter a string: ")
result = reverse_string(spam)
print("reversed string: ", result)



''' another way,

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
'''