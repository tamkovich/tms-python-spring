# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 12345-> 23451.

list_1 = [1, 2, 3, 4, 5]
list_2 = []
i = 0

while i < len(list_1):
    j = list_1.pop()
    list_2.append(j)
print(list_2)

# метод for
list_1 = [1, 2, 3, 4, 5]
list_2 = []

for i in range(len(list_1)):
    j = list_1.pop()
    list_2.append(j)
print(list_2)
