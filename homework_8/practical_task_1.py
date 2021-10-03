num_of_days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Date:

    def __init__(self, date_string):
        Date.date_string = date_string

    @classmethod
    def converter(cls):
        cls.number = int(cls.date_string[:2])
        cls.month = int(cls.date_string[3:5])
        cls.year = int(cls.date_string[6:10])

    @staticmethod
    def validator():
        if Date.month > 12 or Date.month <= 0:
            print('Некорректное значение месяца!')
        elif Date.number > num_of_days_in_months[Date.month - 1] or Date.number <= 0:
            print('Некорректное значение дня!')
        elif Date.year <= 0:
            print('Некорректное значение года!')
        else:
            print('Валидная дата!')


date = Date('11-13-2012')
print(date.date_string)
date.converter()
date.validator()

date = Date('41-11-2012')
print(date.date_string)
date.converter()
date.validator()

date = Date('11-12--012')
print(date.date_string)
date.converter()
date.validator()

date = Date('11-12-2012')
print(date.date_string)
date.converter()
date.validator()
