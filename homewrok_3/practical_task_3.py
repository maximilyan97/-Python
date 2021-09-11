def my_func(num_1, num_2, num_3):
    """Возвращает сумму двух наибольших чисел из трех переданных."""
    if num_1 <= num_2:
        if num_3 >= num_1:
            return num_2 + num_3
        else:
            return num_1 + num_2
    else:
        if num_2 >= num_3:
            return num_2 + num_1
        else:
            return num_1 + num_3


numbers = list(map(int, input('Введите три числа через пробел: ').split()))

print(f'Сумма двух наибольших введенных чисел - {my_func(numbers[0], numbers[1], numbers[2])}')
