class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Зарплата сотрудника: {sum([value for value in self._income.values()])}')


worker = Position('Иван', 'Иванов', 'Главный инженер', 30000, 14000)

worker.get_total_income()
worker.get_full_name()

