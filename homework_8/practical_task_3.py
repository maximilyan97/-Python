class NumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


lst = []

while True:
    try:
        element = input('Введите элемент, который хотите добавить в список. Если хотите выйти введите stop: ')
        if element == 'stop':
            break
        if not element.isdigit():
            raise NumberException('Введенный элемент не число!')
        else:
            lst.append(int(element))

    except NumberException as err:
        print(err)

print(f'Итоговый список: {lst}')
