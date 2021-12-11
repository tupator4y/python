from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)

            with open ("my_dict.json", "w", encoding="utf-8") as f_json:
                my_list = zip_longest((" ".join(u.split(",")) for u in users), hobby, fillvalue=None)
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in my_list}

                dump(my_dict, f_json, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)