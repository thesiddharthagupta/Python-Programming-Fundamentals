text = "cat dog cat bird dog cat"

words = text.lower().split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

sortedWords = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(sortedWords[:10])
