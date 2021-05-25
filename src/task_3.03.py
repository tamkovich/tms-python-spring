# Ввести предложение состоящее из двух слов. Поменять
# местами слова, добавить восклицательный знак в начало
# и конец, вывести итоговое предложение на экран.

string = input()
string = string.split(' ')
string = string[1], string[0]
string = list(string)
string.append('!')
string.insert(0, '!')
print(' '.join(string))
