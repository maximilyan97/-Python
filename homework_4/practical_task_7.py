def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        yield res


num_n = int(input('Введите число n: '))

count = 1
for el in fact(num_n):
    print(f'{count}! = {el}')
    count += 1
