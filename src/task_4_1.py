# 1) Дан список целых чисел.
# Создать новый список, каждый элемент которого
# равен исходному элементу умноженному на -2.

num = [1, 22, 3, 10, 38, 11]
num_while = []
index = 0

while index < len(num):
    num_while.append(num[index] * -2)
    index += 1
print(num_while)

num_for = []
for i in range(len(num)):
    num_for.append(num[i] * -2)
print(num_for)
