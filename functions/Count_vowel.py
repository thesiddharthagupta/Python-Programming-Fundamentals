def count_vowels(spam):
    count = 0
    for ch in spam:
        if ch.lower() in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")
result = count_vowels(text)
print("Number of vowels:", result)

