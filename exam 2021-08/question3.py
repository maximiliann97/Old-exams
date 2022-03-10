class Interval:
    def __init__(self, low, high):
        if high < low:
            raise ValueError("high must be larger or equal to low")
        self.low = low
        self.high = high

    def __repr__(self):
        return f'Interval({self.low},{self.high})'

    def overlaps(self, other):
        return self.high >= other.low and other.high >= self.low

    def __float__(self):
        return (self.high + self.low)/2

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __add__(self, other):
        return Interval(self.low + other.low, self.high + other.high)

    def __sub__(self, other):
        return Interval(self.low - other.high, self.high - other.low)

    def __mul__(self, other):
        # Compute all 4 extremes
        values = self.low*other.low, self.low*other.high, self.high*other.low, self.high*other.high
        return Interval(min(values), max(values))



# Test code
x = Interval(1., 3.)
y = Interval(-4., 5.)
z = Interval(-10., 0.)
print('x overlaps z =', x.overlaps(z))
print('y overlaps z =', x.overlaps(y))
print('-x = ', -x)
print('-y = ', -y)
print('-z = ', -z)
print('x + y =', x + y)
print('x - y =', x - y)
print('z - x =', z - x)
print('x * y =', x * y)
print('z * y =', z * y)
print('y * y =', y * y)
print('float(x) =', float(x))
print('float(y) =', float(y))
print('float(z) =', float(z))
