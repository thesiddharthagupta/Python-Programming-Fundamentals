t = (1, 2, 3, 2, 4, 1, 5)

unique_list = []

for item in t:
    if item not in unique_list:
        unique_list.append(item)

new_tuple = tuple(unique_list)

print(new_tuple)
