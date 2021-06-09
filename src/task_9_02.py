""" Задача 9.2.
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""

result = (lambda **kwargs:
          {key * 2: value for key, value in kwargs.items()})(asd=1, dsa=6876, cvc=123, b128=456)

print(result)
