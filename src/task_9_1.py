"""
Homework - 09
task_9_1: Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""
list_str = ["сферический", "конь", "в", "вакууме"]
new_list_str = [f"{i} - {string}" for i, string in enumerate(list_str, 1)]
print(list_str)
print(new_list_str)
