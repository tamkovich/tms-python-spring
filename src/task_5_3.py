# 3) Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300
diapazo_chis = list(range (200, 301))
ult_box = []
box = []
pari = 0
ind = 0
friend_chis = []
for i in diapazo_chis:
    sum_delit = 0
    j = 1
    for j in range(1, 301):
        if j >= i:
            break
        if i % j == 0:
           sum_delit += j
    ult_box.append(sum_delit)
for z in diapazo_chis:
    pari = [z, ult_box[ind]]
    box.append(pari)
    ind += 1
for u in box:
    for t in box:
        if u[0] == t[1] and u[1] == t[0]:
            friend_chis.append(u[0])
print(friend_chis)
