with open('file_for_practical_task_5.txt', 'w+', encoding='utf-8') as file:
    file.write(' '.join(input('Введите список чисел через пробел:').split()))
    file.seek(0)
    print(f'Сумма чисел в файле равна: {sum(map(int, file.read().split()))}')
