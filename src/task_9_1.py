"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""

list_elements = ['krokodil', 'cat', 'dog']
new_list = (lambda j: [f'{i} - {list_elements}' for i, list_elements in enumerate(j, start=1)])
print(list(new_list(list_elements)))
