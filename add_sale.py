from sys import argv

with open("bakery.csv", "a+", encoding="utf-8") as sales_a:
    with open("bakery.csv", "r", encoding="utf-8") as sales_r:
        if len(argv) > 1 and [n for n in argv[1:] if "." in n and n.replace(".", "").isdigit()]:
        # if len(argv) > 1:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f"{round(float(argv[1]), 3):>010}", file=sales_a)
            else:
                print("Должно быть меньше 99999.999")
        else:
            print(sales_r.read())
