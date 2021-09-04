start_result = float(input('Введите начальный результат спортсмена: '))

wish_result = float(input('Введите желаемый результат спортсмена: '))

num_of_day = 1
cur_result = start_result

while cur_result < wish_result:
    cur_result = 1.1 * cur_result
    num_of_day += 1

print('Номер дня когда результат спортсмена станет не хуже желаемого: ', num_of_day)
