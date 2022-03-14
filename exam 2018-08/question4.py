import abc


class Matrix(metaclass=abc.ABCMeta):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    @abc.abstractmethod
    def transpose(self):
        pass

    @abc.abstractmethod
    def __getitem__(self, i):
        pass


class DenseMatrix(Matrix):
    def __init__(self, values, transposed=False):
        self.values = values
        self.transposed = self.transposed
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

    def __getitem__(self, pos):
        pass


class BandedMatrix(SymmetricMatrix):
    def __init__(self, band_values):
        self.band_values = band_values
        self.width = len(self.band_values[0])
        n = len(self.band_values)
        super().__init__(n, n)

    def __getitem__(self, pos):
        row, col = sorted(pos)
        offset = row - col
        if offset >= self.width:
            return 0
        else:
            return self.band_values[row][offset]