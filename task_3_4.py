# Ввести строку. Вывести на экран букву, которая находится в середине этой
# строки.
# Также, если эта центральная буква равна первой букве в строке, то создать и
# вывести часть строки между первым и последним символами исходной строки.
# (подсказка: для получения центральной буквы, найдите длину строки и разделите
# ее пополам. Для создания результирующий строки используйте срез)
a = input()
print(len(a))
b = (len(a)-1) // 2
print(a[b])
if a[b] == a[0]:
    print(a[1:-1])