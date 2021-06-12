"""
    Функция принимает в себя неаграниченое количество чисел
    создает сисок из них, и формирет новый список из нечетных
    чисел
"""
# Функция декаратор
def decorator_proverki(func ):
    # Функция подмены
    def func_value(*args):
        # Что получила функция подмены
        func(args)
        # Создание списка при помощи filter с нечетными значениями
        a = list(filter(lambda x: x % 2 != 0, args))
        return a

    return func_value


@decorator_proverki
def crete_tuple(args):
    print(f"функция получила кортеж: {args}")

    # Вводимыe пользователем числа


print(f"Получен список c удаленными четными значениями: {crete_tuple(1,3,6,7,9,4,2)}")
