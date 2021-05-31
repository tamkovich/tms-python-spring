from random import randint

list_number = []
for k in range(19):
    list_number.append(randint(0, 100))
print(list_number)
count = 0
monotonost = 0
for index, value in enumerate(list_number):
    if index + 1 >= len(list_number):
        break
    elif value >= list_number[index + 1] and index != 0 and monotonost > 0:
        monotonost = 0
        count += 1
    elif value < list_number[index + 1]:
        monotonost += 1
        continue
print(f"{count} участков масива монотонно возрастающих (не меньше пары)")
