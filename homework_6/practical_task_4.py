class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина  поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость данного автобиля {str(self.speed)}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость данного автобиля {str(self.speed)}')
        if self.speed > 60:
            print('Скорость превышена!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость данного автобиля {str(self.speed)}')
        if self.speed > 40:
            print('Скорость превышена!')


class PoliceCar(Car):
    def show_warning(self):
        print('ЭТО ПОЛИЦЕЙСКАЯ МАШИНА! ОСТОРОЖНО')


class SportCar(Car):
    def increase_speed(self):
        self.speed += 5


car = Car(80, 'синий', 'феррари', False)
print(f'Цвет данной машины - {car.color}, марка - {car.name}')
car.go()
car.stop()
car.turn('налево')
car.show_speed()

town_car = TownCar(70, 'белый', 'волга', False)
print(f'Цвет данной машины - {car.color}, марка - {car.name}')
town_car.go()
town_car.stop()
town_car.turn('налево')
town_car.show_speed()

work_car = WorkCar(50, 'желтый', 'мерседес', False)
print(f'Цвет данной машины - {car.color}, марка - {car.name}')
work_car.go()
work_car.stop()
work_car.turn('направо')
work_car.show_speed()

police_car = PoliceCar(65, 'белый', 'рено', True)
print(f'Цвет данной машины - {car.color}, марка - {car.name}')
police_car.go()
police_car.stop()
police_car.turn('направо')
police_car.show_speed()
police_car.show_warning()

sport_car = SportCar(65, 'зеленый', 'ламборджини', False)
print(f'Цвет данной машины - {car.color}, марка - {car.name}')
sport_car.go()
sport_car.stop()
sport_car.turn('налево')
sport_car.show_speed()
sport_car.increase_speed()
sport_car.show_speed()
