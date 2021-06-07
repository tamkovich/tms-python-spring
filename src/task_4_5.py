"""Составить список чисел Фибоначчи содержащий 15 элементов."""
spis_ok = []
spis_ok_2 = []
i = 0
d = 1
b = 1
z = 0
while i < 15:
    spis_ok.append(z)
    z = d + b
    d = b
    b = z
    i += 1
print(spis_ok, len(spis_ok))
d = 1
b = 1
z = 0
for cikl in range(0, 15):
    spis_ok_2.append(z)
    z = d + b
    d = b
    b = z
print(spis_ok_2, len(spis_ok_2))