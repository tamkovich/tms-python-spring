# Два натуральных числа называют дружественными,
# если каждое из них равно сумме всех делителей другого,
# кроме самого этого числа.
# Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300


min_number = 200
max_number = 300


# Функция возвращает сумму делителей числа n
def summa(n):
    opr = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            opr += k
    return opr


# Подсчет суммы делителей всех натуральных чисел от 2 до max_number
lst = [0, 1]
for m in range(2, max_number + 1):
    lst.append(summa(m))

# Поиск дружественных чисел
for i in range(2, max_number + 1):
    for j in range(i + 1, max_number + 1):
        if i == lst[j] and j == lst[i]:
            print(i, j)
