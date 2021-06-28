# Homework - 05
# Задание 5.07  (HW) Написать игру. Пользователь угадывает число.
# Сперва вводиться диапазон угадывания. После колличество попыток.
# При правильном ответе - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить:
# You are the loser и правильное число.
from random import randint

nach_diap = input("Введите начало диапозона угадывания: ")
if nach_diap.isdigit():
    nach_diap = int(nach_diap)
else:
    print("Начало диапозона введено не корректно!")
    exit()
kon_diap = input("Введите конец диапозона угадывания: ")
if kon_diap.isdigit():
    kon_diap = int(kon_diap)
else:
    print("Конец диапозона введен не корректно!")
    exit()
if kon_diap <= nach_diap:
    print("Диапозон введен не корректно!")
    exit()
popytki = input("Введите количество попыток: ")
if popytki.isdigit():
    popytki = int(popytki)
else:
    print("Количество попыток введено не корректно!")
    exit()
shans = 1
numb = randint(nach_diap, kon_diap)
while popytki >= shans:
    num_user = input("Введите угадываемое число: ")
    if num_user.isdigit():
        num_user = int(num_user)
        if num_user == numb:
            print("You are the winner.")
            break
        elif num_user > numb:
            print("Угадываемое число меньше введенного!")
            shans += 1
            continue
        else:
            print("Угадываемое число больше введенного!")
            shans += 1
            continue
    else:
        print("Вводите число!")
        break
else:
    print("You are the loser.")
    print(f"Угадываемое число: {numb}")
