# Задание 1.1
# Создать переменные firstname, lastname, age с соответствующими значениями
# Путем сложения получить строку вида: 'Привет, меня зовут Иван Иванов, мне 35 лет'
# Примечание: переменную age задавать как строку ‘35’

firstname = 'Иван'
lastname = 'Иванов'
age = 35
print('Привет, я ' + firstname + ' ' + lastname + ', мне ' + str(age) + ' лет')
greeting = ('Привет, я ' + firstname + ' ' + lastname + ', мне ' + str(age) + ' лет')
message = f'Привет, я {firstname} {lastname}, мне {age} лет'
print(message)
print(len(message))
# попробовал 2 способа получения строки + посчитал количество символов
