# """В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы"""
stroka = "good girl, Adel"
mas_strok = stroka.split(' ')
mas_strok = ' '.join(list(reversed(mas_strok)))
print(stroka)
print(mas_strok)
