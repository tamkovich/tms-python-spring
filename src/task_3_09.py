# Задание 3.09
# Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
# D = b2 – 4ac;
# x1,2 = (-b +/- sqrt (D)) / 2a
# Предусмотреть 3 варианта:
# 1) Два действительных корня
# 2) Один действительный корень
# 3) Нет действительных корней

print("Calculating the roots of a quadratic equation",
      "ax\u00B2 + bx + c = 0 \n",
      "Please input the coefficients", sep="\n")

a, b, c = input("a = "), input("b = "), input("c = ")

nums = set('1234567890-.')  # Set of allowed characters in strings which represents a numbers


# ---------- Checking a, prepare for convert to float ----------

a = a.replace(",", ".")
a = a.replace("+", "")


# If set a_set contains elements not included in set nums,
# then the intersection of sets a_set and nums will not coincide with set a_set

a_set = set(a)
is_correct_char = (a_set & nums) == a_set

is_correct_separator = a.count(".") <= 1
is_correct_sign = a.count("-") >= 0 & a.find("-") <= 0
is_correct_a = is_correct_char & is_correct_separator & is_correct_sign


# ---------- Checking b, prepare for convert to float ----------

b = b.replace(",", ".")
b = b.replace("+", "")

b_set = set(b)
is_correct_char = (b_set & nums) == b_set

is_correct_separator = b.count(".") <= 1
is_correct_sign = b.count("-") >= 0 & b.find("-") <= 0
is_correct_b = is_correct_char & is_correct_separator & is_correct_sign

# ---------- Checking c, prepare for convert to float ----------

c = c.replace(",", ".")
c = c.replace("+", "")

c_set = set(c)
is_correct_char = (c_set & nums) == c_set

is_correct_separator = c.count(".") <= 1
is_correct_sign = c.count("-") >= 0 & c.find("-") <= 0
is_correct_c = is_correct_char & is_correct_separator & is_correct_sign

if not (is_correct_a & is_correct_b & is_correct_c):
    print("Coefficients is incorrect!")
elif float(a) == 0 and float(b) != 0:
    print(f"The equation is not quadratic, but the root is {round(-float(c) / float(b), 2)}")
elif float(a) == 0 and float(b) == 0:
    print("There is no roots!")
else:
    a, b, c = float(a), float(b), float(c)
    d = b ** 2 - 4 * a * c
    sign_1, sign_2 = "+" if b >= 0 else "", "+" if c >= 0 else ""
    print(f"\n{a}x\u00B2{sign_1}{b}x{sign_2}{c} = 0")
    print(f"D = b\u00B2 - 4ac = {d}\n")

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f"There is two roots: \n  x\u2081 = {round(x1, 2)},  x\u2082 = {round(x2, 2)}")
    elif d == 0:
        x1 = -b / (2 * a)
        print(f"There is one root: \n  x = {round(x1, 2)}")
    else:
        print(f"There is two complex roots... but this is another one story. ;-)")
