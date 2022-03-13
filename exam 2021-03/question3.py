from math import cos, sin, pi
import numpy as np


class CosineSeries:
    def __init__(self, coef: list):
        self.coef = coef

    def __repr__(self):
        return 'CosineSeries({})'.format(self.coef)

    def __iter__(self):
        return iter(self.coef)

    def __len__(self):
        return len(self.coef)

    def evaluate_term(self, i, x):
        if i < 0:
            raise IndexError('Negative index')
        if i >= len(self.coef):
            return 0
        return self.coef[i]*cos(2*pi*i*x)

    @staticmethod
    def __add_coefficients(list1, list2):
        while len(list1) > len(list2):
            if len(list1) == len(list2):
                break
            list2.append(0)

        while len(list2) > len(list1):
            if len(list2) == len(list1):
                break
            list1.append(0)
        array1 = np.array(list1)
        array2 = np.array(list2)
        added_list = list(array1+array2)
        return added_list

    def __add__(self, other):
        return CosineSeries(self.__add_coefficients(self.coef, other.coef))

    def __iadd__(self, other):
        self.coef = self.__add_coefficients(self.coef, other.coef)
        return self

    def __call__(self, x):
        s = 0
        for i, c in enumerate(self):
            s += c*cos(2*pi*i*x)
        return s



a = CosineSeries([1., 2., 3.])
b = CosineSeries([4., 6.])
print("a(0.5) =", a(0.5))
print("repr(b) =", repr(b))
c = CosineSeries([2., 2.])
c += a
d = b + CosineSeries([1., 1., 1., 1.])
print("c.evaluate_term(0, 0.5) =", c.evaluate_term(0, 0.5))
print("c.evaluate_term(1, 0.5) =", c.evaluate_term(1, 0.5))
print("c.evaluate_term(2, 0.5) =", c.evaluate_term(2, 0.5))
assert c.evaluate_term(3, 0.5) == 0
assert c.evaluate_term(4, 0.5) == 0
try:
    c.evaluate_term(-1, 0.5)
except IndexError as e:
    print('IndexError:', e)
print(f"d has {len(d)} non-zero coefficients")
print("Coefficients of d:", end='')
for coefficient in d:
    print(coefficient, end='')
print()