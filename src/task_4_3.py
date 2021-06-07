#  Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
n = 0
while n < 4:
    key = list(a.keys())
    y = key.pop(n)
    z = str(len(y))
    s = str(y) + z
    a[s] = a.pop(y)
    n += 1
print(a)

dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(dct.keys()):
    dct[key + str(len(key))] = dct.pop(key)
print(dct)
