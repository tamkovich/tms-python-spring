# Создать два списка произвольного содержания.
# Добавить к каждому списку по одному элементу в конец и в начало.
# Расширить первый список вторым.
# Все изменения выводить на экран.


first_list = ['правят']

print(first_list)

first_list.append('этим миром')

print(first_list)

first_list.insert(0, 'Котики')

print(first_list)

second_list = ['Котики']

print(second_list)

second_list.append('рулят')

print(second_list)

second_list.insert(0, 'и конечно же')

print(second_list)

first_list.extend(second_list)

print(first_list)
