"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков

"""
list_of_word = ["int", "begin", "string", "boolean", "float"]
print(([f"{i} - {word}" for i, word in enumerate(list_of_word, 1)]))
