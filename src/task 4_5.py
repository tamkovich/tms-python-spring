# Задание 4_5
# Составить список чисел Фибоначчи, содержащий 15 элементов
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа
# равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34...

# while:
print('Вариант с while:')
list_fib = []
i = 0
while i < 15:
    if i == 0 or i == 1:
        list_fib.append(1)
    else:
        list_fib.append(list_fib[i - 1] + list_fib[i - 2])
    i += 1
print(list_fib)

# for:
print('Вариант с for:')
list_fib = []
for i in range(0, 15):
    if i == 0 or i == 1:
        list_fib.append(1)
    else:
        list_fib.append(list_fib[i - 1] + list_fib[i - 2])
    i += 1
print(list_fib)
