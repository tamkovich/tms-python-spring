print("введите n", end=" ")
n = int(input())
print("введите m", end=" ")
m = int(input())
list_del_number = []
for i in range(n, m + 1):
    for j in range(2, i):
        if i % j == 0:
            list_del_number.append(j)
    print(f"{i}: {list_del_number}")
    list_del_number.clear()
