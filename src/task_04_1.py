# Задание 4.1
# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2

# Using while loop
src_list = [1, 12, 11, 9, 7, 0, 19, 77]
res_list = []

print(f"Source list: {src_list}")

while src_list:
    res_list.append(src_list.pop() * (-2))

res_list = res_list[::-1]
print(f"Source list multiplied (-2):\n{res_list}")

# Using for loop
src_list = [1, 12, 11, 9, 7, 0, 19, 77]
res_list = []

for elem in src_list:
    res_list.append(elem * (-2))

print(res_list)
