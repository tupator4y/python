with open("nginx_logs.txt", "r", encoding="utf-8") as f_text:
    parsed = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f_text)
    for n in parsed:
        print(n)