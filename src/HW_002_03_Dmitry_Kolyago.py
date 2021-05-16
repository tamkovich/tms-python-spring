'''
-------------------------------------------------------------------------------
ЗАДАНИЕ 2.03

Создать список из двух элементов.
Создать кортеж из двух элементов.
Создать словарь с одной парой. Ключ - кортеж, значение - список
Создать словарь с одной парой. Ключ - список, значение - кортеж
-------------------------------------------------------------------------------
'''
# A list with two items

list_1 = ['one', 'two']
print(f'\nThe list: {list_1}')

# A Tuple with two items

tuple_1 = (1, 2)
print(f'The tuple: {tuple_1}')


# A dictionary with one pair where the key is a tuple and the value is a list

dict_1 = {tuple_1: list_1}
print(f'The dict: {dict_1}\n')


# Attempt to create a dictionary with one pair
# where the key is a list and the value is a tuple:
# results in an error cause the key unable to be of variable data type (list)

# dict_2 = {list_1: tuple_1}
