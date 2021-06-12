#Дано число. Найти сумму и произведение его цифр
namber = '5678'
list_namber = []
proizved_namber = 1
sum_namber = 0
for i in namber:
    list_namber.append(i)
for j in list_namber:
    proizved_namber *= int(j)
    sum_namber += int(j)
print('произведение цифр - ', proizved_namber)
print('сумма цифр - ', sum_namber)
