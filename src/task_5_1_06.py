# Задание 5.6
# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]

from random import randint

src_list = []
list_size = 30
mono_intervals = []
need_scan = True

for i in range(list_size):
    src_list.append(randint(1, 500))
src_list.append(0)
print(f"Source array:\n{src_list[:-2]}\n")

start_index = 0
while need_scan:
    index = start_index + 1

    while (src_list[index] > src_list[index - 1]) and index < len(src_list) - 1:
        index += 1

    if (index - start_index) > 1:
        mono_intervals.append(src_list[start_index: index])

    start_index = index
    need_scan = start_index < len(src_list) - 1

print(f"Number of monotonic intervals: {len(mono_intervals)}")
print(mono_intervals)
