num = int(input('Введите целое положительное число: '))

max_digit = num % 10

while True:
    num = int(num / 10)

    if num == 0:
        break

    cur_digit = num % 10

    if cur_digit > max_digit:
        max_digit = cur_digit

print('Максимальная цифра введенного числа: ', max_digit)

