"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

func = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})
print(func(abc=5))
