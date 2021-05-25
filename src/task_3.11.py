# Ввести почтовый адрес. Проверить доменной имя. В случае если оно
# gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’

email = input()
domain = email.split('@')
domain = domain[1]
if domain == 'gmail.com':
    print(domain)
else:
    print('DOMAIN NAME is not supported')
