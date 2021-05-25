# Запросить у пользователя возраст. Если возраст меньше
# 0 - вывести Wrong input, если меньше 18 - вывести
# CocaCola, иначе - вывести Beer

age = int(input('Your age is: '))
if age < 0:
    print('Wrong input')
elif age < 18:
    print('CocaCola')
else:
    print('Beer')
