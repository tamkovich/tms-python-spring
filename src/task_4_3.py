# Задание 4.3
# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()


# Using for loop
src_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
result_dict = {}

for key, value in src_dict.items():
    result_dict.update({f"{key}{len(key)}": value})

src_dict = result_dict.copy()
result_dict.clear()
print(src_dict)

# Using while loop
src_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

while src_dict:
    item = src_dict.popitem()
    result_dict.update({f"{item[0]}{len(item[0])}": item[1]})

src_dict = result_dict.copy()
result_dict.clear()
print(src_dict)
