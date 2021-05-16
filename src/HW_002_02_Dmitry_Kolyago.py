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
