# Задание 4.2
# Дан список целых чисел. Подсчитать сколько четных чисел в списке


# Using while loop
src_list = [1, 12, 11, 9, 7, 0, 19, 77, 100, 122]
cnt_even = 0

print(f"Source list: {src_list}")

while src_list:
    cnt_even += int(src_list.pop() % 2 == 0)

print(f"Count of even numbers: {cnt_even}")

# Using for loop
src_list = [1, 12, 11, 9, 7, 0, 19, 77, 100, 122]
cnt_even = 0

for elem in src_list:
    cnt_even += int(elem % 2 == 0)

print(f"Count of even numbers: {cnt_even}")
