# В семье N свадьба. Они решили выбрать заведение, где будут праздновать в
# зависимости от количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, а если
# меньше 20 то отпраздную дома.
# Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей (прочитать
# переменную с консоли)


N = int(input('Введите количество ваших гостей:'))
if N > 50:
    print('Гоу в ресторан')
elif 20 < N:
    print('Идем в кафе')
else:
    print('Празднуем дома')
