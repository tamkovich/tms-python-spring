#"""получить на ввод колличесто рублей и копеек и вывести в правильной форме"""
vvod = input("введите колличество рублей и копеек через точку ")
vvod = vvod.split('.')
a = vvod[0]
b = vvod[1]
result = []
if int(a) == 1:
    a += " ruble "
    result += a
else:
    a += " rubles "
    result += a
if int(b) == 1:
    b += " kopek"
    result += b
else:
    b += " kopeks"
    result += b
print(' '.join(result))
