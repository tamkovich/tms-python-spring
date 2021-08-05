""" 4. Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный. """


def decorator_(func):
    """Декоратор меняет порядок аргументов на противоположный"""
    def inner(*args):
        print(f"входящие аргументы - {args}")
        resultat = func(*args[::-1])
        print(f"исходящие аргументы - {resultat}")
        return resultat

    return inner


@decorator_
def start_list_numbers(*args):
    """Ф-ия принимает аргументы"""
    return args


if __name__ == "__main__":
    start_list_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
