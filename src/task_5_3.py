""" Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys().
(подсказка: создается новый ключ с цифрой в конце, старый удаляется) """

# while loop
abc = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys_abc = list(abc.keys())
value_abc = list(abc.values())
i = 0
while i < len(abc):
    del abc[keys_abc[i]]
    abc[keys_abc[i] + str(len(keys_abc[i]))] = value_abc[i]
    i += 1
print(abc)

# for loop
jj = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_j = {}
for key, value in jj.items():
    new_j[key + str(len(key))] = value
print(new_j)
