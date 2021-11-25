price_list = [20.19, 11.02, 3.50, 23.23, 44.0, 24.52, 10.56, 2.20, 99.99, 93.2, 69.69, 6.9, 75.57, 6.06, 53.5, 23.01,
              24.6, 5.06, 44.4, 23.53]

for n in price_list:
    rub, kop = f"{n:.2f}".split(".")
    print(f"{rub} руб {kop} коп,", end=" ")

print("\n\n", "B:")
print("price_list ID:", (id(price_list)), price_list)
price_list.sort()
print("price_list ID:", (id(price_list)), price_list)

print("\n", "C:")
reverse_list = sorted(price_list, reverse=True)
print("reverse_list ID:", (id(reverse_list)), price_list)

print("\n", "D:")
print(f"{reverse_list[:5][::-1]}")

#может надо было вместе с "руб, коп" вывести?..