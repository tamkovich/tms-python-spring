from statistics import geometric_mean

# Нахождения среднего арифметического и геометрического
def fun_1(*args, mean_type):
    if mean_type == 1:
        return float(sum(args)) / max(len(args), 1)
    elif mean_type == 2:
        return geometric_mean(args)

print("1. Среднего арифметического")
print("2. Среднего геометрического")
num = input()
if num.isdigit():
    if int(num) == 1:
        print(f"Среднего арифметического: {fun_1(1, 5, 7, mean_type = 1)}")
    else:
        print(f"Среднего геометрического: {fun_1(1, 5, 7, mean_type = 2)}")
