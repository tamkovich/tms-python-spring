"""
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
"""
print("Используем цикл While: ")
money = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
spisok_keys = list(money.keys())
spisok_values = list(money.values())
i = 0
while i < len(money):
    del money[spisok_keys[i]]
    money[spisok_keys[i] + str(len(spisok_keys[i]))] = spisok_values[i]
    i += 1
print(money)
print("\nИспользуем цикл For: ")
money = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
spisok_keys = list(money.keys())
spisok_values = list(money.values())
for i in range(len(money)):
    del money[spisok_keys[i]]
    money[spisok_keys[i] + str(len(spisok_keys[i]))] = spisok_values[i]
print(money)
