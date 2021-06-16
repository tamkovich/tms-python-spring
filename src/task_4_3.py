# Homework - 04
# task_4_3:
# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

sl1 = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub"}
sl2 = {}
kl = list(sl1.keys())
zn = list(sl1.values())
while kl:
    a = kl.pop(0)
    b = f"{a}{str(len(a))}"
    sl2[b] = zn.pop(0)
print(f"Изменённый словарь 1: {sl2}")

slov1 = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub"}
slov2 = {}
kluch = list(slov1.keys())
znach = list(slov1.values())
for i in kluch:
    c = f"{i}{str(len(i))}"
    slov2[c] = znach.pop(0)
print(f"Изменённый словарь 2: {slov2}")
