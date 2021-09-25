from time import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(f'Текущий цвет светофора {self.__color}')
        start_time = time()
        if self.__color == 'зеленый':
            while time() - start_time < 10:
                pass
            self.__color = 'красный'
        elif self.__color == 'красный':
            while time() - start_time < 7:
                pass
            self.__color = 'желтый'
        elif self.__color == 'желтый':
            while time() - start_time < 2:
                pass
            self.__color = 'зеленый'


start_color = input('Введите стартовый цвет светофора: ')
time_of_work = input('Введите желаемое время работы светофора: ')
traffic_light = TrafficLight(start_color)
print(f'Запускаем работу светофора на {time_of_work} сек.')
st_time = time()
while time() - st_time < float(time_of_work):
    traffic_light.running()
print('Работа светофора завершена!')
