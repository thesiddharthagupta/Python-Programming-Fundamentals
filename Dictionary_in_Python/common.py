d1 = {"a":1, "b":2, "c":3}
d2 = {"b":5, "c":7, "d":9}

print("Keys of d1:", d1.keys())
print("Keys of d2:", d2.keys())

common = d1.keys() & d2.keys()  # -> & refer for common 

print("Common keys:", common)