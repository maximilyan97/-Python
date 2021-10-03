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
        self.dict_of_office_equipment[str(thing.__dict__)] -= number
        print(f'{thing} в количестве {number} отправлен в отдел {subsection}')


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


# Создадим склад
warehouse = OfficeEquipmentWarehouse({})
# Создадим принтер
printer = Printer('Принтер Samsung VX13-72', 2012, True)
# Создадим ксерокс
xerox = Xerox('Ксерокс LG 1313', 2014, 'A4')
# Создадим сканнер
scanner = Scanner('Сканнер Lenovo 11', 2021, 3)

# Отправим 3 принтера на склад
warehouse.acceptance_of_equipment(printer, 3)
print(warehouse.dict_of_office_equipment)
# Отправим 2 ксерокса на склад
warehouse.acceptance_of_equipment(xerox, 2)
print(warehouse.dict_of_office_equipment)
# Отправим 4 сканнера на склад
warehouse.acceptance_of_equipment(scanner, 4)
print(warehouse.dict_of_office_equipment)
# Заберем со склада 2 принтера и отправим в подразделение "Бухгалтерия"
warehouse.send_to_subsection(printer, 2, 'Бухгалтерия')
print(warehouse.dict_of_office_equipment)



