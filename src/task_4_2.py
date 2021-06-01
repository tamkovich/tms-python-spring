# 2) Дан список целых чисел. Подсчитать сколько четных чисел в списке.

num = [1, 22, 3, 10, 38, 11, 24]
i = 0

while num:
    if num.pop() % 2 == 0:
        i += 1
print(i)

num = [1, 22, 3, 10, 38, 11, 24]
i = 0

for j in range(len(num)):
    if num.pop() % 2 == 0:
        i += 1
print(i)
print(j)
