# Дан список. Создать новый список, сдвинутый на 1 элемент влево
print("Используем цикл While: ")
spisok = [1, 2, 3, 4, 5]
i = 0
x = spisok[0]
while i < (len(spisok)-1):
    spisok[i] = spisok[i+1]
    i += 1
spisok[len(spisok)-1] = x
print(spisok)
print("\nИспользуем цикл For: ")
spisok = [1, 2, 3, 4, 5]
x = spisok[0]
for i in range(len(spisok)-1):
    spisok[i] = spisok[i + 1]
    i += 1
spisok[len(spisok) - 1] = x
print(spisok)
