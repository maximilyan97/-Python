from sys import argv


def get_salary(num_of_hours, hourly_rate, monthly_bonus):
    """Возвращает зарплату сотрудника за месяц, рассчитанную по выработке в часах, ставке в час и премии."""
    return num_of_hours * hourly_rate + monthly_bonus


script_name, name, surname, hours, rate, bonus = argv

print(f'Зарплата сотрудника {name} {surname}: {get_salary(int(hours), float(rate), float(bonus))} р.')

