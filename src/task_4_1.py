"""Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2"""
spisok = list(range(1, 45))
new_spisok = []
new_new_spisok = []
i = 0
while i < len(spisok):
    new_spisok.append(spisok[i] * -2)
    i += 1
print(new_spisok)
for f in spisok:
    new_new_spisok.append(f * -2)
print(new_new_spisok)
