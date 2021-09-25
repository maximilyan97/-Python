class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Это ручка!')


class Pencil(Stationery):
    def draw(self):
        print('Это карандаш!')


class Handle(Stationery):
    def draw(self):
        print('Это маркер!')


st = Stationery('Кисточка')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

st.draw()
pen.draw()
pencil.draw()
handle.draw()
