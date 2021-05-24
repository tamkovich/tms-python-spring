a = input("Введите строку: ")
b = int(len(a) / 2)
print(a[b])
if a[b] == a[0]:
    print(a[1:-1])