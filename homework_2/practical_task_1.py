lst = [1, 'a', True, ['b', 'c'], ('d', 'e'), {'name': 'Maxim', 'age': 23}]

for i in range(len(lst)):
    print(f'{i + 1}й элемент списка типа {type(lst[i])}')
