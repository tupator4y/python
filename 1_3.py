num = 1

while num <= 100:
    second_digit = num % 10
    first_digit = num // 10

    if second_digit == 1 and first_digit != 1:
        print(num, 'процент')

    if 2 <= num <= 4 or 2 <= second_digit <= 4 and first_digit != 1:
        print(num, 'процента')

    if second_digit > 4 or second_digit == 0 or first_digit == 1:
        print(num, 'процентов')

    # print(num, first_digit, second_digit)

    num += 1