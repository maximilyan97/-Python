def sum_of_numbers(current_sum, numbers):
    """Возвращает сумму текущего значения суммы и новых введенных пользователем чисел."""
    for number in numbers:
        current_sum += int(number)
    return current_sum


cur_sum = 0
spec_character = '!'

while True:
    str_of_numbers = input('Введите строку чисел, разделенных пробелом: ').split()
    if spec_character in str_of_numbers:
        cur_sum = sum_of_numbers(cur_sum, str_of_numbers[:str_of_numbers.index(spec_character)])
        print(f'Итоговая сумма: {cur_sum}')
        break

    cur_sum = sum_of_numbers(cur_sum, str_of_numbers)
    print(f'Текущая сумма: {cur_sum}')
