"""Дан список. Создать новый список, сдвинутый на 1 элемент влево"""
lis_t = list(range(0, 22))
new_lis_t = []
new_lis_t_2 = []
i = -1
z = -1
while i < len(lis_t) - 1:
    new_lis_t.append(lis_t[i])
    i += 1
print(new_lis_t)
for b in lis_t:
    new_lis_t_2.append(lis_t[z])
    z += 1
print(new_lis_t_2)
