# 3) Дан словарь:
# {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys().

# метод while
dict_1 = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
i = 0

while i < len(dict_1):
    del dict_1[dict_keys[i]]
    dict_1[dict_keys[i] + str(len(dict_keys[i]))] = dict_values[i]
    i += 1
print(dict_1)

# метод for
dict_1 = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())

for i in range(len(dict_1)):
    del dict_1[dict_keys[i]]
    dict_1[dict_keys[i] + str(len(dict_keys[i]))] = dict_values[i]
print(dict_1)
