src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# result = [23, 1, 3, 10, 4, 11]

new_dict = {n: 0 for n in src}

for n in src:
    new_dict[n] += 1

print([n for n in new_dict if new_dict[n] == 1])