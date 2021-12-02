from requests import get, utils
from datetime import datetime
from sys import argv

page = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(cur):
    urlsplit = page.split("<Valute ID=")

    for n in urlsplit:
        if cur.upper() in n:
            print(cur.upper(), end=" ")
            print(float(n.replace("/", "").split("<Value>")[1].replace(",", ".")), ", ", sep="", end="")
            print(datetime.strptime(urlsplit[0].split('"')[-4], '%d.%m.%Y').date(), "\n", sep="", end="")


if __name__ == "__main__":
    val = argv[1]
    print(currency_rates(val))
