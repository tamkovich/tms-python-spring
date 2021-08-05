""" 3. Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка """


def decorator_(func):

    def inner(*args):
        print(f"входящие данные - список чисел {args}")
        resultat = list(filter(lambda x: x % 2 != 0, func(*args)))
        print(f"исходящие данные - список нечетных чисел {resultat}")
        return resultat
    return inner


@decorator_
def start_list_numbers(list_numbers: list) -> list:
    """Ф-ия принимает список чисел."""
    return list_numbers


if __name__ == "__main__":
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start_list_numbers(list_numbers)
