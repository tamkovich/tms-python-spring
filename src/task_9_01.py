""" Задача 9.1.
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков
"""

STRINGS = ["Python", "Java", "JavaScript", "Ruby"]

fmtd_strings = [f"{i} - {string}" for i, string in enumerate(STRINGS)]

print(f"Source list:\n{STRINGS}\n")
print(f"Formatted list:\n{fmtd_strings}")
