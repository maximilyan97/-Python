from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def fabric_consumption(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumption(self):
        return 2 * self.h + 0.3


sum_fabric_consumption = 0

while True:
    type_of_clothes = input('Выберите тип одежды. Введите 1, если тип одежды - пальто, введите 2, если тип'
                            ' одежды - костюм, введите q, если хотите закончить добавлять одежду для рассчета '
                            'суммарного расхода ткани: ')
    if type_of_clothes == '1':
        coat = Coat(float(input('Вы выбрали пальто. Введите размер человека: ')))
        sum_fabric_consumption += coat.fabric_consumption
    elif type_of_clothes == '2':
        suit = Suit(float(input('Вы выбрали костюм. Введите рост человека: ')))
        sum_fabric_consumption += suit.fabric_consumption
    elif type_of_clothes == 'q':
        break
    else:
        print('Выберите корректный пункт меню!')

print(f'Ввод одежды для рассчета суммарного расхода ткани на одежду завершен. '
      f'Суммарный расход ткани на одежду: {sum_fabric_consumption}')
