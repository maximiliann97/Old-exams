import abc


class Matrix(metaclass=abc.ABCMeta):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    @abc.abstractmethod
    def transpose(self):
        pass

    @abc.abstractmethod
    def __getitem__(self):
        pass


class DenseMatrix(Matrix):
    def __init__(self, values, transposed = False):
        self.values = values
        self.transposed = transposed
        if self.transposed:
            super().__init__(len(self.values[0]), len(self.values))
        else:
            super().__init__(len(self.values), len(self.values[0]))

    def transpose(self):
        return DenseMatrix(self.values, not self.transposed)

    def __getitem__(self, pos):
        if self.transposed:
            pos = pos[::-1]
        return self.values[pos[0]][pos[1]]


class SymmetricMatrix(Matrix):
    def transpose(self):
        return self

