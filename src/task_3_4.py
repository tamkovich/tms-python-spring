"""
Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
Также, если эта центральная буква равна первой букве в строке,
то создать и вывести часть строки между первым и последним символами исходной строки.
"""
str = input("Введите строку: ")
sr_str = str[int(len(str) / 2)]
print(sr_str)
print(str[0])
if sr_str == str[0]:
    str_new = input("Введите новую строку: ")
    print(str_new[1:int((len(str_new)-1) / 2)])
