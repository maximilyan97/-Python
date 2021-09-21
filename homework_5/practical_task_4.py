with open('file_r_for_practical_task_4.txt', 'r', encoding='utf-8') as file_r,\
        open('file_w_for_practical_task_4.txt', 'w', encoding='utf-8') as file_w:
    numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for line in file_r:
        lst = line.split()
        lst[0] = numbers[lst[0]]
        file_w.write(' '.join(lst) + '\n')
