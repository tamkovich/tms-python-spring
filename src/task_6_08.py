"""  В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы. """

stroka = "1aaa 2bb 3c 4dd 5eee 6ffff"
spisok_iz_stroki = stroka.split(" ")
new_stroka = ""
i = len(spisok_iz_stroki) - 1
while i >= 0:
    if i > 0:
        new_stroka += spisok_iz_stroki[i] + " "
    else:
        new_stroka += spisok_iz_stroki[i]
    i -= 1
print(new_stroka)
