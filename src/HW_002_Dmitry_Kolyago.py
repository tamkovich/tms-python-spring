'''
-------------------------------------------------------------------------------
ЗАДАНИЕ 2.01

Создать переменные firstname, lastname, age с соответствующими значениями
Путем сложения получить строку вида: Привет, меня зовут Иван Иванов, мне 35 лет
Примечание: переменную age задавать как строку ‘35’
-------------------------------------------------------------------------------
'''

firstname = 'Иван'
lastname = 'Иванов'
age = '35'

msg = f'\nПривет, меня зовут {firstname} {lastname}, мне {age} лет.\n'
print(msg)


'''
-------------------------------------------------------------------------------
ЗАДАНИЕ 2.02

Создать два списка произвольного содержания.
Добавить к каждому списку по одному элементу в конец и в начало.
Расширить первый список вторым.
Все изменения выводить на экран.
-------------------------------------------------------------------------------
'''

list_1 = [1, 2, 3, 4]
list_2 = [7, 8, 9]

# Modifying list_1

print(f'\nOriginal List_1: {list_1}')
list_1.append(5)
print(f'List_1 with item appended to the end: {list_1}')

list_1.insert(0, 0)
print(f'List_1 with item inserted to the head: {list_1}\n')


# Modifying list_2

print(f'Original List_2: {list_2}')
list_2.append(10)
print(f'List_2 with item appended to the end: {list_2}')

list_2.insert(0, 6)
print(f'List_2 with item inserted to the head: {list_2}\n')


# Extending list_1 with list_2

list_1.extend(list_2)
print(f'List_1 extended with list_2: {list_1}\n')

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

'''
-------------------------------------------------------------------------------
ЗАДАНИЕ 2.04

Создать два списка a = [1,2,3,4] и b = [ ]
Вывести на экран id a и b
Присвоить b значение a (b=a)
Вывести на экран id переменных
Добавить элемент в список b
Вывести на экран оба списка
-------------------------------------------------------------------------------
'''
a = [1, 2, 3, 4]
b = []

info = (f'\nid(a): {id(a)}\n'
        f'id(b): {id(b)}\n'
        f'id(a) = id(b): {id(a) == id(b)} \n')
print(info)

b = a
info = (f'id(a): {id(a)}\n'
        f'id(b): {id(b)}\n'
        f'id(a) = id(b): {id(a) == id(b)} \n')
print(info)


b.append('new_one')
print(f'\nList a: {a}\nList b: {b}')

a.append('next_one')
print(f'\nList a: {a}\nList b: {b}\n')