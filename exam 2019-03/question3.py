import numpy as np


class OuterMatrix:
    def __init__(self, u, v):
        self.u = u.copy()
        self.v = v.copy()

    def toarray(self):
        return np.outer(self.u, self.v)

    def transpose(self):
        return OuterMatrix(self.v, self.u)

    def norm(self):
        return np.linalg.norm(self.u)*np.linalg.norm(self.v)

    def __getitem__(self, pos):
        row, col = pos
        if type(row) == slice and type(col) == slice:
            return OuterMatrix(self.u[row], self.v[col])
        else:
            return self.u[row] * self.v[col]

    def __mul__(self, value):
        if type(value) in [float, int]:
            return OuterMatrix(value * self.u, self.v)
        elif type(value) == np.ndarray:
            if len(value.shape) > 1:
                raise Exception("Can only multiply by 1D NumPy arrays")
            return np.dot(self.u, value) * self.v
        else:
            raise TypeError("Can only multiply by scalar or 1D NumPy arrays")

    def __imul__(self, value):
        if type(value) not in [float, int]:
            raise ValueError('Value must be int or float')
        self.u *= value
        return self


a = np.array([9., 1., 2., 3., 4., 5., 6.])
b = np.array([2., 1., 4., 3., 6., 5., 7.])
c = np.array([1., 2., 1., 7., 8., 2., 4.])
m = OuterMatrix(a, b)
print("Expanded:\n{}".format(m.toarray()))
m_sub = m[1:3, 2:5] # This should also be a OuterMatrix.
print("Slicing (expanded):\n{}".format(m_sub.toarray()))
print("Slicing:", m[1:3, 5]) # slice + int -> ndarray
print("Slicing:", m[3, 2:5]) # int + slice -> ndarray
print("Item:", m[2, 4]) # int + int -> float
print("Norm:", m.norm())
m *= 2
print("Norm after scaling:", m.norm())
print("Multiplication with array:", m * c)
m_sub_t = m_sub.transpose()
print("Transpose (expanded):\n{}".format(m_sub_t.toarray()))

