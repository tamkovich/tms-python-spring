#  В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы

string = 'one two three four five six seven eight nine ten'
list_1 = string.split(' ')
[list_1.insert(i, list_1.pop()) for i in range(len(list_1))]
print(list_1)
