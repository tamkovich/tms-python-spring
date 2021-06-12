""" 
    Программа при помощи анонимной функции
    создает словарь с неограничеными ключ значениями
    где ключ равняеться удвоенной длине 
"""
func = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(func(a=2, b=4))
