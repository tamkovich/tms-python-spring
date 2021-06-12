# В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.

string = 'каждый охотник желает знать где сидит фазан'

new_str = string.split()

i = len(new_str) - 1
result = ''
while i >= 0:
    i -= 1
    result += new_str[i] + ' '
print(result)
