# from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        my_list = zip_longest(users, hobby, fillvalue=None)

        with open ("users_hobby.txt", "w", encoding="utf-8") as f_text:
            for n in my_list:
                print(f"{str(n[0]).strip()}: {str(n[1]).strip()}", file=f_text)