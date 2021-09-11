def func_of_division(number_1, number_2):
    """Выводит частное от деления и отслеживает деление на ноль.

    Позиционные параметры:
    number_1 -- делимое
    number_2 -- делитель

    """
    if number_2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(f'Результат деления: {number_1 / number_2}')


num_1 = float(input('Введите делимое: '))
num_2 = float(input('Введите делитель: '))

func_of_division(num_1, num_2)
