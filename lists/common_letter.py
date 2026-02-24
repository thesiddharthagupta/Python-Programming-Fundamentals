text = "banana"

result = {}

for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print(result)