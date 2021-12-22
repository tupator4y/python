from random import choice

class Car:
    def __init__(self, name, color, speed, cop=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.cop = cop
        print(f'Новая машина: {name}, цвет "{color}".\nЭто копы? {cop}\n')

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}'

    def go(self):
        print(f'{self.name}: Поехали!')

    def stop(self):
        print(f'{self.name}: Остановочка!')

    direction = ['направо', 'налево', 'назад']

    def turn(self):
        print(f'{self.name}: Поворотик {choice(self.direction)}.')

class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}. ШТРАФ!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}. ШТРАФ!' if self.speed > 60 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, cop=True)


car_police = PoliceCar("РОСГВАРДИЯ", "чёрный", 200)
car_work = WorkCar("Мусоровоз", "белый", 40)
car_sport = SportCar("Лада Веста", "чёрный", 200)
car_town = TownCar("Лада 99", "металлик", 200)

cars = [car_town, car_sport, car_work, car_police]

for i in cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()