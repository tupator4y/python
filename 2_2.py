tmp_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for n in tmp_list:
    if n.replace("+", "").isdigit():
        if n.isdigit():
            new_list.append(f"'{int(n):02}'")
        else:
            new_list.append(f"'{n[0]}{int(n[1:]):02}'")
    else:
        new_list.append(n)

print(new_list)
print(' '.join(new_list))

# пытался сделать так, но после разбора дз, понял, что надо было прочитать про f строки... и про
# кавычки слушать... :3

# print(len(tmp_list[1]))
# print(tmp_list[1].startswith("0"))
# tmp_list[n].startswith("5")
# tmp_list.insert(1, '"')

# for n in range(len(tmp_list)):
    # while tmp_list[n].isdigit() or tmp_list[n][1:].isdigit():
    #     print(n, "is dig")
    #     tmp_list.insert(1, '"')
    #     n += 1
    # if tmp_list[n].isdigit() and len(tmp_list[n]) == 1:
    #     tmp_list[n] = tmp_list[n].zfill(2)
    # if tmp_list[n].startswith("+"):
    #     tmp_list[n] = tmp_list[n].zfill(3)
    # if tmp_list[n].isdigit():
    #     print((tmp_list[n].isdigit()))
    #     tmp_list.insert(0, '"')

# for i, val in enumerate(tmp_list):
    # if tmp_list[i][1:].isdigit():
        # print(i, 'is  dig')
        # tmp_list.insert(i, '"')