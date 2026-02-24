tup1 = (2,3,4,16,12,18,31)
tup2 = (2,3,41,16,11,48,71)

common = []

for item in tup1:
    if item in tup2:
        common.append(item)
print("Common Element: ", common)