"""
 Создать lambda функцию, которая принимает на вход неопределенное
 количество именных аргументов и выводит словарь с ключами удвоенной
 длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""

funct = (lambda **slovar: {key * 2: value for key, value in slovar.items()})(penal=5, dinozavr=6, pistolet=7)

print(funct)
