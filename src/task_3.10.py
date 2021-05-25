# Получить на ввод количество рублей и копеек и вывести в правильной
# форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки

while True:
    money = input('Sample input: 2,31\n'
                  '              5,86\n'
                  '              0,44\n'
                  'Enter your cash: ')

    #

    if '.' or ',' in money:
        money = money.replace(',', '.').split('.')

    rub = ''
    coin = ''

    try:
        if money[0] != '0':
            if 5 <= int(money[0]) <= 20:
                rub = money[0] + ' рублей'
            elif int(money[0]) % 10 == 1:
                rub = money[0] + ' рубль'
            elif 2 <= int(money[0]) % 10 <= 4:
                rub = money[0] + ' рубля'
            elif 5 <= int(money[0]) % 10 <= 9:
                rub = money[0] + ' рублей'
            elif int(money[0]) % 10 == 0:
                rub = money[0] + ' рублей'
        else:
            pass
    except ValueError:
        print('Wrong input!')

    try:
        if money[1] != '':
            if 5 <= int(money[1]) <= 20:
                coin = money[1] + ' копеек'
                print(rub, coin)
            elif int(money[1]) % 10 == 1:
                coin = money[1] + ' копейка'
                print(rub, coin)
            elif 2 <= int(money[1]) % 10 <= 4:
                coin = money[1] + ' копейки'
                print(rub, coin)
            elif 5 <= int(money[1]) % 10 <= 9:
                coin = money[1] + ' копеек'
                print(rub, coin)
            elif int(money[1]) % 10 == 0:
                coin = money[1] + ' копеек'
                print(rub, coin)
        else:
            pass
    except IndexError:
        print(rub)
