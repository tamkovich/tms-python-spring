# Задание 2_2
# Даны действительные числа x и y. Получить |x| - |y| / 1 + |xy|

x = 2
y = 1
diff = abs(x) - abs(y)
summ = 1 + abs(x * y)
reply = diff / summ
print(reply)
