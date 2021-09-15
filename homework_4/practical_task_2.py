lst = input('Введите список чисел через пробел: ').split()

print(f'Отфильтрованный список: {[int(num) for i, num in enumerate(lst) if int(num) > int(lst[i - 1]) and i > 0]}')
