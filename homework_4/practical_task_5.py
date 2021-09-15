from functools import reduce

print(f'Результат произведения всех четных чисел от 10 до 100 включительно: ' +
      f'{reduce(lambda num_1, num_2: num_1 * num_2, [i for i in range(10, 101) if i % 2 == 0])}')
