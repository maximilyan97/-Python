time_in_sec = int(input('Введите время в секундах: '))

time_in_min = int(time_in_sec / 60)
num_of_sec = time_in_sec % 60
num_of_hours = int(time_in_min / 60)
num_of_min = time_in_min % 60

print(f'Время в формате чч:мм:сс: {num_of_hours:02}:{num_of_min:02}:{num_of_sec:02}')
