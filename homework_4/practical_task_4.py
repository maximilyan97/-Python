lst = input('Введите список чисел: ').split()

print(f'Список из элементов без повторений: {[int(num) for num in lst if lst.count(num) == 1]}')
