list_number_1 = []
list_number_2 = []

i = 200
n = 201

for d in range(1, i):
    if i % d == 0:
        list_number_2.append(d)
while True:
    for m in range(1, n):
        if n % m == 0:
            list_number_1.append(m)

    if sum(list_number_2) == n and sum(list_number_1) == i:
        if sum(list_number_2) == 1:
            list_number_2.clear()
            list_number_1.clear()
        else:
            print(
                f"пара дружественых чисел{n, i}, делители этих чисел {list_number_1 , list_number_2}"
            )
            print(
                f"сумма делителей этих чиселл {sum(list_number_1), sum(list_number_2)}"
            )
            list_number_2.clear()
            list_number_1.clear()
    else:
        list_number_1.clear()
    n += 1
    if n > 300:
        i += 1
        list_number_2.clear()
        for d in range(1, i):
            if i % d == 0:
                list_number_2.append(d)
        n = i + 1
    if i > 300:
        break
