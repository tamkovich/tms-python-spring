"""Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()"""
slovar = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}
kopia = {'test': 'test_value',
          'europe': 'eur',
          'dollar': 'usd',
          'ruble': 'rub'}
a = list(slovar.keys())
b = list(slovar.values())
schetchik = 0
schetchik_2 = 0
new_key_2 = ''
for i in kopia:
    d = str(i) + str(len(i))
    del slovar[str(i)]
    slovar[d] = b[schetchik]
    schetchik += 1
print(slovar)
while schetchik_2 < len(slovar):
    new_key_2 = str(a[schetchik_2]) + str(len(a[schetchik_2]))
    del kopia[str(a[schetchik_2])]
    kopia[new_key_2] = b[schetchik_2]
    schetchik_2 += 1
print(kopia)
