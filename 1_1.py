duration = 23462748

d = duration // 86400
h = duration % 86400 // 3600
m = duration % 3600 % 3600 // 60
s = duration % 60

print(d, 'дней,', h, 'часов,', m, 'минут,', s, 'секунд')