# Ввести число, проверить на то, что было введено именно
# число. Возвести его в куб.

num = input()
if num.isdigit():
    num = int(num) ** 3
    print(num)
else:
    print('Wrong input')
