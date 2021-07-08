"""
Homework - 09
task_9_2: Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""
old_dict = {"abc": 5, "def": 8, "xyz": 13}
new_dict = (lambda **kwargs: dict((key * 2, value) for key, value in old_dict.items()))
print(new_dict())
