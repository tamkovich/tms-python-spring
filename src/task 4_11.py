# Задание 3_11
# Ввести почтовый адрес
# Проверить доменное имя
# В случае если оно gmail.com, вывести на экан имя почтового ящика
# Иначе вывести надпись 'DOMAIN NAME is not supported'

gmail = input('Ввести почтовый адрес: ')
dom = gmail.split('@')
print(dom)
dom = dom[1]
if dom == 'gmail.com':
    print(gmail)
else:
    print('DOMAIN NAME is not supported')