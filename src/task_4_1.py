"""
Дан список целых чисел. Создать новый список, каждый
элемент которого равен исходному элементу умноженному на -2
"""
print("Используем цикл While: ")
number = [2, 12, -7, 16, 8]
number_new = []
i = 0
while i < len(number):
    number_new.append(number[i] * -2)
    i += 1
print(number_new)
number_new = []
print("\nИспользуем цикл For: ")
# Запуск цикл по элементом списка
for num in number:
    # элемент списка умнажается на -2
    number_new.append(num * -2)
print(number_new)
