def my_func_1(num_x, num_y):
    """Возвращает число x в степени y."""
    num_y = -num_y
    result = 1
    for i in range(num_y):
        result *= num_x

    return 1 / result


def my_func_2(num_x, num_y):
    """Возвращает число x в степени y."""
    return num_x ** num_y


x = float(input('Введите действительное положительное х: '))
y = int(input('Введите целое отрицательное у: '))

print(f'х в степени у, вычисленное первым способом: {my_func_1(x, y)}')

print(f'х в степени у, вычисленное вторым способом: {my_func_2(x, y)}')
