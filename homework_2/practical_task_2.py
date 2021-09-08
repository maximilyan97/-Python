lst = input('Введите элементы списка через пробел: ').split()

print(f'Начальный список: {lst}')
count = 0

while count < (len(lst) - len(lst) % 2):
    additional_var = lst[count]
    lst[count] = lst[count + 1]
    lst[count + 1] = additional_var

    count += 2

print(f'Перемешанный список: {lst}')
