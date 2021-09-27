class Matrix:
    def __init__(self, list_of_strings):

        self.list_of_strings = list_of_strings

    def __str__(self):

        return str(self.list_of_strings).replace("],", "],\n")

    def __add__(self, other):

        return Matrix([[self.list_of_strings[i][j] + other.list_of_strings[i][j] for j in
                        range(len(self.list_of_strings[i]))] for i in range(len(self.list_of_strings))])


matrix_1 = Matrix([[2, 3, 4, 5], [4, 5, 5, 1], [4, 5, 1, 2]])
matrix_2 = Matrix([[7, 1, 0, 1], [2, 3, 2, 3], [1, 2, 3, 4]])

print(matrix_1)
print(matrix_2)

print(f'Сумма двух матриц:\n{matrix_1 + matrix_2}')


