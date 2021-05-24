# Ввести предложение. Если число символов в
# предложении кратно 3 - добавить ! к концу строки.
# Вывести строку на экран.

string = input()
if len(string) % 3 == 0:
    string = list(string)
    string.append("!")
print(''.join(string))
