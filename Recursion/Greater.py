#grater among 3

def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c
a = 3
b = 18
c = 12

print("the greater value is: ", greater(a,b,c))