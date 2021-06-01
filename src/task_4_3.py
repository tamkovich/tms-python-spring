# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

dict_1 = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}

keys, values, i = list(dict_1.keys()), list(dict_1.values()), 0
dict_1_items = dict_1.items()

# ------------------------WHILE----------------------------------------

while i < len(dict_1):
    key = keys[i]
    del dict_1[key]
    dict_1[f'{key}{str(len(key))}'] = values[i]
    i += 1
print(dict_1)

# -------------------------FOR-----------------------------------------

dict_1 = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}

for i in range(len(dict_1)):
    key = keys[i]
    del dict_1[key]
    dict_1[f'{key}{str(len(key))}'] = values[i]
print(dict_1)
