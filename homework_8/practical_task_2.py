class ZeroDivisionException(Exception):

    def __init__(self, txt):
        self.txt = txt


try:
    divisible = float(input('Введите делимое: '))
    divisor = float(input('Введите делитель: '))
    if divisor == 0:
        raise ZeroDivisionException("На ноль делить нельзя!")
    print(f'Частное: {divisible / divisor}')
except ZeroDivisionException as err:
    print(err)
