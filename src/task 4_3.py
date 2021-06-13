# Задание 4_3
# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {'key': 'value'} -> {'key3': 'value'})
# Чтобы получить список ключей - использовать в конце метод .keys()
# (подсказка: создаётся новый ключ с цифрой в конце, старый удаляется)

# while:
print('Вариант с while:')
dict_1 = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}
dict_keys = dict_1.keys()
dict_values = dict_1.values()
keys = list(dict_keys)
values = list(dict_values)
i = 0
dict_new = {}
while dict_1:
    if i < len(keys):
        key = keys[i]
        dict_new[key + str(len(key))] = values[i]
        i += 1
    else:
        break
print(dict_new)

# for:
print('Вариант с for:')
dict_1 = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}
dict_new = {}
for key, value in dict_1.items():
    dict_new[key + str(len(key))] = value
print(dict_new)
