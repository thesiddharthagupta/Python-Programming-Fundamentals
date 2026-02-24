def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]

    for num in lst:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [10, 5, 20, 3, 15]

mx, mn = find_max_min(numbers)

print("Max:", mx)
print("Min:", mn)




"""
numbers = [10, 5, 20, 3, 15]

maximum = max(numbers)
minimum = min(numbers)

print("Max:", maximum)
print("Min:", minimum)

"""