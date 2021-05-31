list_number = [1, 2, 3, 4, 5]
new_list_number = []
for i in list_number:
    new_list_number.append(i * -2)

print(new_list_number)
i = 0
new_list_number_2 = []
while len(list_number) > i:
    new_list_number_2.append(list_number[i] * -2)
    i += 1
print(new_list_number_2)
