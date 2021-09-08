rating = []

while True:
    print('1 - Добавить элемент в рейтинг. 2 - Вывести рейтинг. 3 - Выход.')
    choice = input('Выберите пункт меню: ')

    if choice == '1':
        elem_of_rating = int(input('Введите элемент, который хотите добавить в рейтинг: '))

        if len(rating) == 0 or rating[-1] >= elem_of_rating:
            rating.append(elem_of_rating)
        else:
            for elem in rating:
                if elem < elem_of_rating:
                    rating.insert(rating.index(elem), elem_of_rating)
                    break

    elif choice == '2':
        print(rating)
    elif choice == '3':
        break
    else:
        print('Выберите существующий пункт меню!')
