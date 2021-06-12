"""
    Функцияя декоратор выполнет замену аргментов
    принимаемой функцией на противоположные
"""
# Фуункция декаратор
def func_wraper(func):
    def wraper(*args, **kwargs):
        func(args, kwargs, "заданны пользователем")
        # Формирование списка с перевернутыми аргументами
        a = list(map(lambda value: value, (list(args) + list(kwargs.keys()))[::-1]))
        # Генерируем args с новыми аргументами
        args = [a[index] for index in range(len(a) - len(kwargs.keys()))]
        b = a[-(len(kwargs.keys())) : :]
        # Генерируем kwargs с новыми аргументами
        kwargs = {b[index]: value for index, value in enumerate(list(kwargs.values()))}
        return func(args, kwargs, "такие аргументы после подмены")

    return wraper


@func_wraper
# Фуункция отображения аргументов до и после замены
def write_args(arg1, arg2, line_start_finish):
    print(f"такие аргументы {line_start_finish}: {arg1} , {arg2}")


# Функция принимает не огрраниченые количество и явно и не явно заданные аргументы
write_args("a", "b", "c", 1, v=2, e=3)
