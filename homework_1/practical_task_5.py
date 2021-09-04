revenue = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if revenue > costs:
    profitability = (revenue - costs) / revenue
    print('Фирма работает с прибылью. Рентабельность выручки: ', profitability)
    num_of_workers = int(input('Введите количество сотрудников: '))
    print('Прибыль в расчете на одного сотрудника: ', (revenue - costs) / num_of_workers)
else:
    print('Фирма работает с убытком.')
