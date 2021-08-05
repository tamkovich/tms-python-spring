""" 2. Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5} """

dict_1 = {'ivavi': 1, 'nana': 2, 'opo': 3}
dict_new = (lambda **kwargs: dict((key * 2, value) for key, value in dict_1.items()))
print(dict_new())
