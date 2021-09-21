with open('file_for_practical_task_3.txt', 'r', encoding='utf-8') as file:
    print('Сотрудники, имеющие оклад меньше 20 тыс.:')
    sum_income = 0
    count_of_workers = 0
    for line in file:
        if int(line.split()[1]) < 20000:
            print(line.split()[0])
        sum_income += int(line.split()[1])
        count_of_workers += 1
    print(f'Средняя величина дохода сотрудников: {(sum_income/count_of_workers).__round__(3)}')
