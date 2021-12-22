class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight=25, thick=5):
        return (self._length * self._width * weight * thick) / 1000


a = Road(5000, 20)

print('Масса асфальта:', (int(a.mass())), 'т')