"""
    Программа выволняет с помощью генератора списка
    перевод index в string и создает новый список
"""

list_str_line = ["index_1", "index_2", "index3", "index_4"]
# Генератор списка
new_list_str_line = [str(index) for index, _ in enumerate(list_str_line)]

print(new_list_str_line)
