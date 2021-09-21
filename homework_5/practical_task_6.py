with open('file_for_practical_task_6.txt', 'r', encoding='utf-8') as file:
    statistics = {}
    for line in file:
        statistics[line.split()[0].replace(":", "")] =\
            sum(map(int, ''.join(ch for ch in line if ch.isdigit() or ch.isspace()).split()))

    print(f'Статистика по предметам: {statistics}')
