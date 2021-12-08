num = int(input("Введите число: "))


def num_gen(num):
    for num in range(1, num + 1):
        if num % 2 != 0:
            yield num

for n in num_gen(num):
    print(n)