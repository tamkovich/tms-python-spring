# Задание 4.3
# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()


# Using for loop
src_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys, values = list(src_dict.keys()), list(src_dict.values())
src_dict.clear()
i = 0

for key in keys:
    src_dict.update({f"{key}{len(key)}": values[i]})
    i += 1

print(src_dict)

# Using while loop
src_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys, values = list(src_dict.keys()), list(src_dict.values())
src_dict.clear()

while keys:
    key = keys.pop()
    src_dict.update({f"{key}{len(key)}": values.pop()})

print(src_dict)
