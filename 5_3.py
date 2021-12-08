from itertools import islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

comp_list = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))

# print(type(comp_list), *comp_list)
# for i in range(len(tutors) + 1):
#     print(next(comp_list))

# print(type(comp_list), *comp_list)

print(*islice(comp_list, len(tutors)))
print(list(islice(comp_list, len(tutors))))