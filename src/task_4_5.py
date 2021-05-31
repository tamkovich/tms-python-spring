list_number = []
for i in range(1, 14):
    if len(list_number) == 0:
        list_number.append(i)
        list_number.append(i)

    list_number.append(list_number[i] + list_number[i - 1])
print(list_number, len(list_number))
list_number_while = []
count = 1
while True:
    if len(list_number_while) == 0:
        list_number_while.append(count)
        list_number_while.append(count)
    elif len(list_number_while) > 14:
        print(list_number_while)
        break
    list_number_while.append(list_number_while[count] + list_number_while[count - 1])
    count += 1
