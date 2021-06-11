# Составить список чисел Фибоначчи содержащий 15 элементов.
print("Используем цикл While: ")
i = 2
number_Fibonachi = [1, 1]
while i < 15:
    number_Fibonachi.insert(i, number_Fibonachi[i - 1] + number_Fibonachi[i - 2])
    i += 1
print(number_Fibonachi)
print("\nИспользуем цикл For: ")
number_Fibonachi = [1, 1]
for i in range(15):
    if i > 1:
        number_Fibonachi.insert(i, number_Fibonachi[i - 1] + number_Fibonachi[i - 2])
    else:
        number_Fibonachi[i] = 1
print(number_Fibonachi)
