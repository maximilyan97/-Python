class OfficeEquipmentWarehouse:
    def __init__(self, dict_of_office_equipment):
        self.dict_of_office_equipment = dict_of_office_equipment

    def acceptance_of_equipment(self, thing, number):
        if str(thing.__dict__) in self.dict_of_office_equipment.keys():
            self.dict_of_office_equipment[str(thing.__dict__)] += number
        else:
            self.dict_of_office_equipment[str(thing.__dict__)] = number
        print(f'{thing} в количестве {number} отправлен на склад')

    def send_to_subsection(self, thing, number, subsection):
        if str(thing.__dict__) not in self.dict_of_office_equipment.keys():
            print('Такой техники нет на складе!')
        elif self.dict_of_office_equipment[str(thing.__dict__)] < number:
            print('Такого количества данной техники нет на складе!')
        else:
            self.dict_of_office_equipment[str(thing.__dict__)] -= number
            print(f'{thing} в количестве {number} отправлен в отдел {subsection}')
            if self.dict_of_office_equipment[str(thing.__dict__)] == 0:
                del self.dict_of_office_equipment[str(thing.__dict__)]


class OfficeEquipment:
    def __init__(self, full_name, year_of_release):
        self.full_name = full_name
        self.year_of_release = year_of_release


class Xerox(OfficeEquipment):
    def __init__(self, full_name, year_of_release, format_of_paper):
        self.format_of_paper = format_of_paper
        super().__init__(full_name, year_of_release)

    def __str__(self):
        return f'{self.full_name} {self.year_of_release} года выпуска, формат бумаги - {self.format_of_paper}'


class Printer(OfficeEquipment):
    def __init__(self, full_name, year_of_release, is_color):
        self.is_color = is_color
        super().__init__(full_name, year_of_release)

    def __str__(self):
        return f'{self.full_name} {self.year_of_release} года выпуска, {"цветной" if self.is_color else "черно-белый"}'


class Scanner(OfficeEquipment):
    def __init__(self, full_name, year_of_release, speed_of_scanning):
        self.speed_of_scanning = speed_of_scanning
        super().__init__(full_name, year_of_release)

    def __str__(self):
        return f'{self.full_name} {self.year_of_release} года выпуска, скорость сканирования - {self.speed_of_scanning}'


def user_input_of_equipment(choice):

    full_name = input('Введите полное имя техники в формате Тип_Фирма_Модель: ')
    while True:
        year_of_release = input('Введите год выпуска техники: ')
        if not year_of_release.isdigit() or int(year_of_release) < 0:
            print('Должно быть введено неотрицательное число! Попробуйте еще раз!')
        else:
            break

    while True:
        number = input('Введите количество единиц техники: ')
        if not number.isdigit() or int(number) <= 0:
            print('Должно быть введено положительное число! Попробуйте еще раз!')
        else:
            break

    if choice == '1':
        is_color = bool(input('Нажмите Enter, если принтер черно-белый, иначе - введите что-нибудь и нажмите Enter: '))
        return Printer(full_name, int(year_of_release), is_color), number
    elif choice == '2':
        speed_of_scanning = int(input('Введите скорость сканирования: '))
        return Scanner(full_name, int(year_of_release), speed_of_scanning), number
    elif choice == '3':
        format_of_paper = input('Введите формат бумаги в виде A{цифра}: ')
        return Xerox(full_name, int(year_of_release), format_of_paper), number


# Создадим склад
warehouse = OfficeEquipmentWarehouse({})
# Для простоты считаем, что у нас на складе хранятся только сканнеры, ксероксы и принтеры
# Режим распределения техники на склад
print('Распределяем технику на склад:')
while True:
    choice = input('МЕНЮ: Выберите необходимый пункт. 1 - Добавить принтер на склад, 2 - сканнер, 3 - ксерокс.'
                   ' Введите stop, если хотите закончить распределять технику на склад: ')
    if choice == 'stop':
        break
    elif choice not in ['1', '2', '3']:
        print('Должен быть выбран корректный пункт меню! Попробуйте еще раз!')
        continue

    thing, number = user_input_of_equipment(choice)
    warehouse.acceptance_of_equipment(thing, int(number))

# Выводим текущее состояние склада
print(f'Текущее состояние склада:\n {warehouse.dict_of_office_equipment}')

# Режим распределения техники со склада в подразделения
print('Распределяем технику со склада в подразделения:')
while True:
    choice = input('МЕНЮ: Введите stop, если хотите закончить отправлять технику со склада в подразделения.'
                   ' Если хотите отправить принтер - введите 1, сканнер - 2, ксерокс - 3: ')
    if choice == 'stop':
        break
    elif choice not in ['1', '2', '3']:
        print('Должен быть выбран корректный пункт меню! Попробуйте еще раз!')
        continue

    thing, number = user_input_of_equipment(choice)
    subsection = input('Введите подразделение, в которое хотите отправить технику со склада: ')
    warehouse.send_to_subsection(thing, int(number), subsection)


# Выводим текущее состояние склада
print(f'Текущее состояние склада:\n {warehouse.dict_of_office_equipment}')