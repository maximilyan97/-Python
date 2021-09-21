with open('file_for_practical_task_1.txt', 'w', encoding='utf-8') as file:
    while True:
        new_str = input('Введите новую строку данных для файла. Если хотите выйти из режима ввода,'
                        ' просто нажмите Enter:')
        if not new_str:
            break
        else:
            file.write(new_str + '\n')


