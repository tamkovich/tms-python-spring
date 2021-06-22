import task_7_01

while True:
    print("1. Дюймы в сантиметры")
    print("2. Сантиметры в дюймы")
    print("3. Мили в километры")
    print("4. Километры в мили")
    print("5. Фунты в килограммы")
    print("6. Килограммы в фунты")
    print("7. Унции в граммы")
    print("8. Граммы в унции")
    print("9. Галлон в литры")
    print("10. Литры в галлоны")
    print("11. Пинты в литры")
    print("12. Литры в пинты")
    converter = int(input('Выберите вариант конвертации: '))
    number = input('\nВнесите данные для конвертации: ')
    try:
        if converter == 1:
            print(f"\n{number} дюймов = {task_7_01.duim_in_cm(int(number))} см\n")
        elif converter == 2:
            print(f"\n{number} см = {task_7_01.cm_in_duim(int(number))} дюймов\n")
        elif converter == 3:
            print(f"\n{number} миль = {task_7_01.mil_in_km(int(number))} км\n")
        elif converter == 4:
            print(f"\n{number} км = {task_7_01.km_in_mi(int(number))} миль\n")
        elif converter == 5:
            print(f"\n{number} фнт = {task_7_01.lb_in_kg(int(number))} кг\n")
        elif converter == 6:
            print(f"\n{number} кг = {task_7_01.kg_in_lb(int(number))} фнт\n")
        elif converter == 7:
            print(f"\n{number} унц = {task_7_01.oz_in_gm(int(number))} гр\n")
        elif converter == 8:
            print(f"\n{number} гр = {task_7_01.gm_in_oz(int(number))} унц\n")
        elif converter == 9:
            print(f"\n{number} гал = {task_7_01.gal_in_l(int(number))} литров\n")
        elif converter == 10:
            print(f"\n{number} литров = {task_7_01.l_in_gal(int(number))} гал\n")
        elif converter == 11:
            print(f"\n{number} пнт = {task_7_01.pt_in_l(int(number))} литров\n")
        elif converter == 12:
            print(f"\n{number} литров = {task_7_01.l_in_pt(int(number))} пнт\n")
        else:
            print('\nФункции не существует\n')
            continue
    except ValueError:
        print('\nОшибка ввода данных\n')

    continuer = input('Продолжить? y/n: ')
    if continuer == 'y':
        continue
    elif continuer == 'n':
        break
