list_from_str = input('Введите строку: ').split()

for i in range(len(list_from_str)):

    if len(list_from_str[i]) > 10:
        list_from_str[i] = list_from_str[i][:10]

    print(f'{i + 1}е слово: {list_from_str[i]}')
