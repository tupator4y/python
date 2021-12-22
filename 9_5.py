class Stationery:
    def __init__(self, title="Рисователь"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Пишем, используя ручку '{self.title}'!")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем, используя карандаш '{self.title}'!")

class Handle(Stationery):
    def draw(self):
        print(f"Отмечаем, используя маркер '{self.title}'!")

a = Stationery()
pen = Pen("HyperPen1000-7")
pencil = Pencil("CAR-0N-DASH")
handle = Handle("Banksy' inc.")

office_things = [a, pen, pencil, handle]

for i in office_things:
    i.draw()