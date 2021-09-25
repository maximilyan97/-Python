class Road:

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calc_mass(self, mass, num):
        print(f'Масса асфальта, необходимая для покрытия дорожного полотна: {mass * num * self._width * self._length}')


length_of_road = input('Введите длину дороги: ')
width_of_road = input('Введите ширину дороги: ')
road = Road(float(length_of_road), float(width_of_road))
mass_for_square_meter = input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: ')
number_of_centimeters = input('Введите число см толщины полотна: ')
road.calc_mass(float(mass_for_square_meter), float(number_of_centimeters))
