# Составить список чисел Фибоначчи содержащий 15 элементов.
a = 0
b = 1
c = 0
while c < 15:
    c += 1
    a, b = b, a + b
    print(a)

x = 0
y = 1
for m in range(1, 16):
    x, y = y, x + y
    print(x)
