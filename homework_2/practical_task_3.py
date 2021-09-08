num_of_month = int(input('Введите номер месяца: '))

dict_of_seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for key, value in dict_of_seasons.items():
    if value.count(num_of_month) > 0:
        print(f'Время года - {key}')
        break

num_of_month = int(input('Введите номер месяца еще раз (можно другого): '))

if num_of_month == 12:
    num_of_month = 0

lst_of_seasons = ['Зима', 'Весна', 'Лето', 'Осень']

print(f'Время года - {lst_of_seasons[num_of_month // 3]}')
