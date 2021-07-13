"""Написать 12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число
2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”."""


def conver_ter():
    while True:
        vibor = int(input("сделайте выбор :\n"
                          "1. Дюймы в сантиметры\n"
                          "2. Сантиметры в дюймы\n"
                          "3. Мили в километры\n"
                          "4. Километры в мили\n"
                          "5. Фунты в килограммы\n"
                          "6. Килограммы в фунты\n"
                          "7. Унции в граммы\n"
                          "8. Граммы в унции\n"
                          "9. Галлон в литры\n"
                          "10. Литры в галлоны\n"
                          "11. Пинты в литры\n"
                          "12. Литры в пинты\n"))
        if vibor == 0:
            print("good bye")
            break
        a = int(input("введите колличество"))
        if vibor == 1:
            result = conv_d_s(a)
            print(result)
        elif vibor == 2:
            result = conv_s_d(a)
            print(result)
        elif vibor == 3:
            result = conv_m_k(a)
            print(result)
        elif vibor == 4:
            result = conv_k_m(a)
            print(result)
        elif vibor == 5:
            result = conv_f_k(a)
            print(result)
        elif vibor == 6:
            result = conv_k_f(a)
            print(result)
        elif vibor == 7:
            result = conv_y_g(a)
            print(result)
        elif vibor == 8:
            result = conv_g_y(a)
            print(result)
        elif vibor == 9:
            result = conv_g_l(a)
            print(result)
        elif vibor == 10:
            result = conv_l_g(a)
            print(result)
        elif vibor == 11:
            result = conv_p_l(a)
            print(result)
        elif vibor == 12:
            result = conv_p_l(a)
            print(result)


def conv_d_s(a):
    b = 2.54
    return a * b


def conv_s_d(a):
    b = 2.54
    return a / b


def conv_m_k(a):
    b = 1.609
    return a * b


def conv_k_m(a):
    b = 1.609
    return a / b


def conv_f_k(a):
    b = 2.205
    return a / b


def conv_k_f(a):
    b = 2.205
    return a * b


def conv_y_g(a):
    b = 28.35
    return a * b


def conv_g_y(a):
    b = 28.35
    return a / b


def conv_g_l(a):
    b = 3.785
    return a * b


def conv_l_g(a):
    b = 3.785
    return a / b


def conv_p_l(a):
    b = 2.113
    return a / b


def conv_l_p(a):
    b = 2.113
    return a * b


conver_ter()
