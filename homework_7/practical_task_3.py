class Cell:

    def __init__(self, number_of_cells):
        if not isinstance(number_of_cells, int):
            print('Количество ячеек должно быть целым числом!')
        else:
            self.number_of_cells = number_of_cells

    def __str__(self):
        return f'Клетка с числом ячеек {self.number_of_cells}'

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print('Разность не больше нуля! Операция не будет выполнена!', end='')
            return ''

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(round(self.number_of_cells / other.number_of_cells))

    def make_order(self, number_of_cells_in_row):
        return (('*' * number_of_cells_in_row + '\n') * int(self.number_of_cells / number_of_cells_in_row) +
                '*' * (self.number_of_cells % number_of_cells_in_row) + '.').replace("\n.", ".")


cell_1 = Cell(12)
cell_2 = Cell(15)
cell_3 = Cell(11.5)  # Проверям, что будет если ввести количество ячеек не в виде целого числа
print(f'Разбиение ячеек первой клетки по рядам:\n{cell_1.make_order(5)}')
print(f'Разбиение ячеек второй клетки по рядам:\n{cell_2.make_order(5)}')
print(f'Результат сложения: {cell_1 + cell_2}')
print(f'Результат вычитания: {cell_2 - cell_1}')
# Кейс, когда у первой клетки число ячеек меньше числа ячеек второй клетки:
print(cell_1 - cell_2)
print(f'Результат умножения: {cell_1 * cell_2}')
print(f'Результат деления: {cell_2 / cell_1}')


