class OfficeEquipmentWarehouse:
    def __init__(self, dict_of_office_equipment):
        self.dict_of_office_equipment = dict_of_office_equipment


class OfficeEquipment:
    def __init__(self, full_name, year_of_release):
        self.full_name = full_name
        self.year_of_release = year_of_release


class Xerox(OfficeEquipment):
    def __init__(self, full_name, year_of_release, format_of_paper):
        self.format_of_paper = format_of_paper
        super().__init__(full_name, year_of_release)


class Printer(OfficeEquipment):
    def __init__(self, full_name, year_of_release, is_color):
        self.is_color = is_color
        super().__init__(full_name, year_of_release)


class Scanner(OfficeEquipment):
    def __init__(self, full_name, year_of_release, speed_of_scanning):
        self.speed_of_scanning = speed_of_scanning
        super().__init__(full_name, year_of_release)


printer = Printer('Принтер Samsung VX13-72', 2012, True)
xerox = Xerox('Ксерокс LG 1313', 2014, 'A4')
scanner = Scanner('Сканнер Lenovo 11', 2021, 3)
print(printer.__dict__)
print(xerox.__dict__)
print(scanner.__dict__)




