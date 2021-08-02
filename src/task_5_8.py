"""
В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы.
"""
s = 'Hello world, i learning python'
print(*reversed(s.split()))
