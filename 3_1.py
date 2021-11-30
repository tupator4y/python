numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(value):
    return numbers.get(value)


print(num_translate(input("Введите число: ")))

    # if key in numbers:
    # key = str(input("Введите число: "))
    #     print(numbers[key])
    # else:
    #     print(None)