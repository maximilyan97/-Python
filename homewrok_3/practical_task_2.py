def print_information(name, surname, year_of_btd, city, email, number):
    """Выводит информацию о пользователе одной строкой."""
    print(f'Имя пользователя - {name}, фамилия - {surname}, год рождения - {year_of_btd}, город - {city}, ' +
          f'email - {email}, номер телефона - {number}')


info = input('Введите информацию (имя, фамилию, год рождения, город, email, номер телефона) о пользователе ' +
             'через пробел: ').split()

print_information(name=info[0], surname=info[1], year_of_btd=info[2], city=info[3], email=info[4], number=info[5])
