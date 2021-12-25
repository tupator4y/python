class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['•' * rows for i in range(self.nums // rows)]) + '\n' + '•' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сумма клеток:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Вычитание клеток:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Меньше ячеек в первой клетке, чем во второй"

    def __mul__(self, other):
        print("Умножение клеток:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Частное клеток:")
        return Cell(self.nums // other.nums)

cell_1 = Cell(150)
cell_2 = Cell(25)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))