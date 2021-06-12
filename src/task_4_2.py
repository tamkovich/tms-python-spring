"""Дан список целых чисел. Подсчитать сколько четных чисел в списке"""
spisok = list(range(1, 100))
i = 0
result = 0
new_result = 0
while i < len(spisok):
    if int(spisok[i]) % 2 == 0:
        result += 1
    i += 1
print("колличесто четных чисел", result)
for s in spisok:
    if s % 2 == 0:
        new_result += 1
print("колличесто четных чисел", new_result)
