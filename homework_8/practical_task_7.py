class ComplexNumber:
    def __init__(self, re, img):
        self.re = re
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.img * other.img,
                             self.re * other.img + self.img * other.re)


complex_number_1 = ComplexNumber(1, -3)
complex_number_2 = ComplexNumber(1, 1)
print(f'Первое комплексное число {complex_number_1.re} {"+" if complex_number_1.img > 0 else "-"} {abs(complex_number_1.img)}i')
print(f'Второе комплексное число {complex_number_2.re} {"+" if complex_number_2.img > 0 else "-"} {abs(complex_number_2.img)}i')

print(f'Сумма двух комплексных чисел: '
      f'{(complex_number_1 + complex_number_2).re} {"+" if (complex_number_1 + complex_number_2).img > 0 else "-"}'
      f' {abs((complex_number_1 + complex_number_2).img)}i')
print(f'Произведение двух комплексных чисел: '
      f'{(complex_number_1 * complex_number_2).re} {"+" if (complex_number_1 + complex_number_2).img > 0 else "-"}'
      f' {abs((complex_number_1 * complex_number_2).img)}i')
