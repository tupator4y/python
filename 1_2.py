cube_list = []
all_sum = 0
cube_list_new = []

for i in range(1, 1000, 2):
    cube_list.append(i ** 3)
# print(cube_list)
for n, val in enumerate(cube_list):
    num_sum = 0
    while val > 0:
        num_sum += val % 10
        val //= 10
    if num_sum % 7 == 0:
        all_sum += cube_list[n]
print(all_sum)

for m in cube_list:
    cube_list_new.append(m + 17)
all_sum = 0
# print(cube_list)
for n, val in enumerate(cube_list_new):
    num_sum = 0
    while val > 0:
        num_sum += val % 10
        val //= 10
    if num_sum % 7 == 0:
        all_sum += cube_list_new[n]
print(all_sum)