""" 1. Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков."""

list_1 = ['ivavi', 'nana', 'opo']
list_new = [f"{i} - {string}" for i, string in enumerate(list_1)]
print(list_new)
