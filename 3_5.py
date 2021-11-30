from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def jokes(j, repeat=False):
    """
    Возвращает шутки, собранные из списков
    
    :param n: кол-вош шуток
    :param repeat: Повтор
    :return: 
    """
    joke_list = []
    new_nouns, new_adverbs, new_adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    min_list = min(new_nouns, new_adverbs, new_adj)

    while j and len(min_list):
        randnum = randrange(len(min_list))
        if repeat:
            joke_list.append(f"{new_nouns.pop(randnum)}, {new_adverbs.pop(randnum)}, {new_adj.pop(randnum)}")
        else:
            joke_list.append(f"{choice(nouns)}, {choice(adverbs)}, {choice(adjectives)}")
        j -= 1
    return joke_list

print(jokes(5, False))