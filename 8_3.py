from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        n_list = [el for el in (*args, *kwargs.values())]
        n = [f"{func.__name__}({el}: {type(el)}" for el in n_list]
        print(*n, *func(*args, **kwargs), sep=",\n")

    return wrapper


@type_logger
def calc_cube(*a, **k):
    n_list = [el for el in (*a, *k.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in n_list]


for i in range(1, 6):
    calc = calc_cube(i)
