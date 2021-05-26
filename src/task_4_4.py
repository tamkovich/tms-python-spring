# Задание 4.4
# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 -> 2 3 4 5 1


# Not using loops
src_list = [1, 2, 3, 4, 5]

res_list = src_list[1:]
res_list.append(src_list[0])

print(f"Source list:\n{src_list}\nShifted lists:\n{res_list}")

# Using while loop
src_list = [1, 2, 3, 4, 5]
res_list = []

while len(src_list) > 1:
    res_list.insert(0, src_list.pop())
res_list.append(src_list.pop())

print(res_list)

# Using for loop
src_list = [1, 2, 3, 4, 5]
res_list = []

for elem in src_list[1:]:
    res_list.append(elem)
res_list.append(src_list[0])

print(res_list)
