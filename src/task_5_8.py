"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
"""
print("Введите строку: ")
stroka = input()
stroka_new = stroka.split(' ')
stroka = ""
for i in stroka_new:
    stroka += i[::-1] + " "
print(stroka)