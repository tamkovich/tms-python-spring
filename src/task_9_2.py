"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""


b = (
    lambda **kwargs: {key + key: value for key, value in kwargs.items()})(a=5, uydyfsg=7, kjhuiev=8)
print(b)
