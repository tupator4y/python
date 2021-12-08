num = int(input("Введите число: "))


def num_gen(num):
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)


num_gen(num)
