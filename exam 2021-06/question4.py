import abc
import numpy as np
import math


class Distribution(metaclass=abc.ABCMeta):
    def __init__(self, offset):
        self.offset = offset

    @abc.abstractmethod
    def __call__(self, x):
        pass

    @abc.abstractmethod
    def random(self):
        pass

    def integrate(self, start, end):
        xs = np.linspace(start, end, 100)
        ys = [self(x) for x in xs]
        return np.trapz(xs, ys)


class NormalDistribution(Distribution):
    def __init__(self, sigma, offset=0):
        super().__init__(offset)
        if sigma <= 0:
            raise ValueError("Sigma may not be <= 0")
        self.sigma = sigma

    def __call__(self, x):
        return (1/(self.sigma * math.sqrt(2*math.pi)))*math.exp(-0.5*((x-self.offset)/self.sigma)**2)

    def random(self):
        return np.random.normal(loc=self.offset, scale=self.sigma)

    def __repr__(self):
        return f'NormalDistribution({self.sigma}, {self.offset})'


class UniformDistribution(Distribution):
    def __init__(self, width, offset=0):
        super().__init__(offset)
        if width <= 0:
            raise ValueError("width may not be <= 0")
        self.width = width

    def __call__(self, x):
        if abs(x-self.offset) <= self.width * 0.5:
            return 1/self.width
        else:
            return 0

    def random(self):
        return np.random.uniform(self.offset - self.width/2, self.offset + self.width/2)

    def integrate(self, start, end):
        s = min(end, self.offset - self.width/2)
        e = max(start, self.offset + self.width/2)
        return (e-s)/self.width

    def __repr__(self):
        return f'UniformDistribution({self.width}, {self.offset})'


nd = NormalDistribution(sigma=0.25, offset=0.25)
print(repr(nd))
print(f'nd(0.3) = {nd(0.3)}')
print(f'nd(1.0) = {nd(1.0)}')
print(f'nd.integrate(0., 0.5) = {nd.integrate(0., 0.5)}')
print([nd.random() for _ in range(10)]) # expect numbers near 0 to 0.5

ud = UniformDistribution(width=0.5, offset=0.25) # covers the interval 0 to 0.5
print(repr(ud))
print(f'ud(0.3) = {ud(0.3)}')
print(f'ud(1.0) = {ud(1.0)}')
print(f'ud.integrate(0., 0.5) = {ud.integrate(0., 0.5)}')
print([ud.random() for _ in range(10)]) # expect numbers within 0 to 0.5