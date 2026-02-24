msg = "apple"
d = {}

for c in msg:
    d[c] = d.get(c, 0) + 1

print(d)