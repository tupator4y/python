from requests import get, utils
from datetime import datetime

page = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(cur):
    valsplit = page.split("<Valute ID=")

    for n in valsplit:
        if cur.upper() in n:
            print(cur.upper(), end=" ")
            print(float(n.replace("/", "").split("<Value>")[1].replace(",", ".")), ", ", sep="", end="")
            print(datetime.strptime(valsplit[0].split('"')[-4], '%d.%m.%Y').date(), "\n", sep="", end="")


currency_rates("USD")
currency_rates("eur")
currency_rates("wrong")