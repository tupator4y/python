def thesaurus(*args):
    names_dict = {}
    for n in sorted(args):
        first = n[0]
        if first in names_dict:
            names_dict[first] += [n]
        else:
            names_dict[first] = [n]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
