# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)

numbers = [1, 2, 3, 4, 5, 56, 57, 78, 3, 45, 56, 10, 231, 232, 67, 43]
counter = []
count = 0

for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1] - 1:
        count += 1
    else:
        counter.append(count)
        count = 0

for n in counter:
    if n > 0:
        count += 1

print(count)




