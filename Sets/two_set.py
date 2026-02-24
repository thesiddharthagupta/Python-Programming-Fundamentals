s1 = {1, 2}
s2 = {3, 4}

pairs = set()

for a in s1:
    for b in s2:
        pairs.add((a,b))

print(pairs)