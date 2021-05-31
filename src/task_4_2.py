list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 11, 13, 14, 15, 16]
count = 0
for i in list_number:
    if i % 2 == 0:
        count += 1
print(count)
i = 0
count_2 = 0
while len(list_number) > i:
    if list_number[i] % 2 == 0:
        count_2 += 1
    i += 1
print(count_2)
