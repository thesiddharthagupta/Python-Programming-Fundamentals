class demo:
    a = 4

o = demo()

print(o.a)  #prints class attributes bcz instance attributes is not present

o.a = 0         #instence attributes is set

print(o.a)      #prints the instance attributes bcoz instance attributes  is present.

print(demo.a)   #prints the class attributes
