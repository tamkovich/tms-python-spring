# Задание 2.4
# Ввести строку с клавиатуры.
# Создать строку равную введенной строке без последних двух символов

user_input = input('Input whatever you want: ')

new_str = user_input[:-2]
print(new_str)
