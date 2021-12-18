import re


def email_parse(address):
    re_mail = re.compile(r'(?P<usernsame>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_mail.match(address):
        raise ValueError(f'wrong address: {address}')
    print(re_mail.match(address).groupdict())

    # for i in ['someone@geekbrains.ru', 'someone@geekbrainsru', 'asdas', 324234, 'as342']:
    #     try:
    #         email_parse(i)
    #     except ValueError as err:
    #         print(err)

    # почему-то не работает ) вроде как ошибка питона 3.10

email_parse(address='someone@geekbrains.ru')
email_parse(address='someone@geekbrainsru')
