spec_characters = ['"', "'", '!', '?', '(', ')', '.', ',', ':', ';']
count_of_strings = 0
with open('file_for_practical_task_2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        for character in spec_characters:
            line = line.replace(character, "")
        count_of_strings += 1
        print(f'Количество слов в {count_of_strings}й строке: {len(line.split())}')

    print(f'Количество строк в файле: {count_of_strings}')







