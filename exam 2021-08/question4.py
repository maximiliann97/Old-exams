import abc


class GeneratorVector(metaclass=abc.ABCMeta):
    def __init__(self, length: int):
        self.length = length

    def __len__(self):
        return self.length

    @abc.abstractmethod
    def __getitem__(self, item):
        pass

    def collect(self):
        return [self[i] for i in range(self.length)]


class ConstantVector(GeneratorVector):
    def __init__(self, constant, length):
        self.constant = constant
        super().__init__(length)

    def __getitem__(self, i: int):
        return self.constant

    def __add__(self, x):
        return ConstantVector(self.constant + x, self.length)

    def __mul__(self, x):
        return ConstantVector(self.constant * x, self.length)

    def __repr__(self):
        return f'ConstantVector({self.constant}, {self.length})'


class LinspaceVector(GeneratorVector):
    def __init__(self, start: float, end: float, length: int):
        self.start = start
        self.end = end
        self.delta = end - start
        super().__init__(length)

    def __getitem__(self, i: int):
        return self.start + (self.delta * i)/float(self.length - 1)

    def __add__(self, x):
        return LinspaceVector(self.start + x, self.end + x, self.length)

    def __mul__(self, x):
        return LinspaceVector(self.start * x, self.end * x, self.length)

    def __repr__(self):
        return f'LinspaceVector({self.start}, {self.end}, {self.length})'


class FunctionVector(GeneratorVector):
    def __init__(self, func, length: int):
        super().__init__(length)
        self.func = func

    def __getitem__(self, i: int):
        return self.func(i)

    def __add__(self, x):
        return FunctionVector(lambda i: self.func(i) + x, self.length)

    def __mul__(self, x):
        return FunctionVector(lambda i: self.func(i) * x, self.length)

    def __repr__(self):
        return f'FunctionVector({self.func}, {len(self)})'



def test_vector(v):
    print("Vector:", v)
    print("Length:", len(v))
    print("At pos 1 and 3:", v[1], v[3])
    print("Collected:", v.collect())
    print("Adding 3")
    v2 = v + 3
    print("Vector:", v2)
    print("Length:", len(v2))
    print("At pos 1 and 3:", v2[1], v2[3])
    print("Collected:", v2.collect())
    print("and mutliplying by 0.5")
    v3 = v2 * 0.5
    print("Vector:", v3)
    print("Length:", len(v3))
    print("At pos 1 and 3:", v3[1], v3[3])
    print("Collected:", v3.collect())
    print("")


cv = ConstantVector(3.5, 5)
test_vector(cv)
lv = LinspaceVector(0.5, 1.5, 5)
test_vector(lv)

from math import sqrt
fv = FunctionVector(sqrt, 5)
test_vector(fv)
