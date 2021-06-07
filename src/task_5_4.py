# """Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число"""
n = 10
u = list(range(0, n))
spis = []
sum = 0
promej_chis = 0
for t in u:
    promej_chis = n - t
    box = [promej_chis, '+', t]
    spis.append(box)
print(spis)