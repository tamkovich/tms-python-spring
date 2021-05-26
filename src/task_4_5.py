# Задание 4.5
# Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
# либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

# Using for loop
seq_starter = 1
seq_len = 15
fib_seq = [seq_starter, seq_starter]

for i in range(1, seq_len - 1):
    fib_seq.append(fib_seq[i] + fib_seq[i - 1])

print(fib_seq)

# Using while loop
seq_starter = 1
seq_len = 15
fib_seq = [seq_starter, seq_starter]
i = seq_starter

while i < seq_len - 1:
    fib_seq.append(fib_seq[i] + fib_seq[i - 1])
    i += 1

print(fib_seq)
