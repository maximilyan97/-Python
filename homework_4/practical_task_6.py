from itertools import count, cycle

start = int(input('Введите число, начиная с которого необходимо выводить числа: '))

num = int(input('Введите количество чисел, которое необходимо вывести: '))

for el in count(start):
    if el == start + num:
        break
    else:
        print(el)

lst = input('Введите элементы списка через пробел: ').split()

num = int(input('Введите количество элементов, которое необходимо вывести: '))

count = 0
for el in cycle(lst):
    if count == num:
        break
    print(el)
    count += 1
