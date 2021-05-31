from random import randint

list_number = []
for k in range(19):
    list_number.append(randint(0, 100))
print(list_number)
print(max(list_number))
for index, value in enumerate(list_number):
    if list_number[index] % 2 == 0:
        list_number[index] = max(list_number)
print(list_number)
