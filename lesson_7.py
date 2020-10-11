# Практическое задание 7.1.

class Matrix:
    def __init__(self, list_1, list_2):
        # self.matrix = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])

print(my_matrix.__add__())

# Практическое задание 7.2.


class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())

# Практическое задание 7.3.


class Cell:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "Cell(size:{})".format(self.size)

    # Перегружаем оператор +
    def __add__(self, other):
        return Cell(self.size + other.size)

    # Перегружаем оператор -
    def __sub__(self, other):
        new_size = self.size - other.size
        if new_size > 0:
            return Cell(new_size)
        else:
            raise ArithmeticError(new_size)

    # Перегружаем оператор *
    def __mul__(self, other):
        return Cell(self.size * other.size)

    # Перегружаем оператор *
    def __truediv__(self, other):
        return Cell(self.size // other.size)

    # string representation
    def make_order(self, ro_size):
        residual = self.size
        stress = ''
        while residual:
            this_size = ro_size if residual >= ro_size else residual
            stress += '*' * this_size
            residual -= this_size
        return stress


c5 = Cell(5)
c6 = Cell(6)

print('add: c5 + c6:', c5 + c6)

print('sub: c6 - c5:', c6 - c5)

try:
    print(c5 - c6)
except ArithmeticError:
    print('sub: c5 - c6: Wrong sub args')

print('mul: c5 * c6:', c5 * c6)
print('div: c5 / c6:', c5 / c6)
print('div: c6 / c5:', c6 / c5)
