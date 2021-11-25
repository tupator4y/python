name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for n in range(len(name_list)):
    word_list = name_list[n].split()
    word_list = (word_list[0].capitalize()), (word_list[-1].capitalize())
    print('Привет, ' + word_list[-1] + '!')