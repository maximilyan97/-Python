products = []
count = 0

while True:

    print('1 - Добавить товар. 2 - Вывести текущий список товаров. 3 - Закончить заполнение списка товаров.')
    choice = input('Выберите пункт меню: ')

    if choice == '1':
        products.append((len(products) + 1, {}))
        products[count][1]['Название'] = input('Введите название товара, который хотите добавить в список: ')
        products[count][1]['Цена'] = input('Введите цену товара, который хотите добавить в список: ')
        products[count][1]['Количество'] = input('Введите количество товара, который хотите добавить в список: ')
        products[count][1]['Ед.'] = input('Введите единицы измерения кол-ва товара, который хотите добавить в список: ')

        count += 1

    elif choice == '2':
        print(products)
    elif choice == '3':
        break
    else:
        print('Выберите существующий пункт меню!')

dict_of_analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед.': []}

for product in products:
    dict_of_analytics['Название'].append(product[1]['Название'])
    dict_of_analytics['Цена'].append(product[1]['Цена'])
    dict_of_analytics['Количество'].append(product[1]['Количество'])
    dict_of_analytics['Ед.'].append(product[1]['Ед.'])

print(f'Аналитика по товарам: {dict_of_analytics}')


