"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
"""
print("Введите строку: ")
stroka_is = input()
stroka_new = stroka_is.split(' ')
stroka_is = ""
for i in stroka_new:
    stroka_is += i[::-1] + " "
print(stroka_is)
