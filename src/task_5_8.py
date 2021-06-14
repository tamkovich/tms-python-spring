"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы.
"""
print("Введите строку: ")
stroka = input()
list_of_words = stroka.split(' ')
stroka = ""
for i in list_of_words:
    stroka += i[::-1] + " "
print(stroka)
