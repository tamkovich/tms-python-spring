""" Ввести строку. Если длина строки больше 10 символов, то создать новую
строку с 3 восклицтельными знаками в конце ("!!!") и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки."""

string_1 = input('Введите строку: ')
a = len(string_1)
if a > 10:
    print('{}{}'.format(a, '!!!'))
else:
    print(string_1[1])
