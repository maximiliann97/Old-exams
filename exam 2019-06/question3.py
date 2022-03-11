class Complex:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.b >= 0:
            sign = '+'
        else:
            sign = '-'
            self.b = self.b*-1
        return f'{self.a} {sign} {self.b}im'

    def real(self):
        return self.a

    def imag(self):
        return self.b

    def __abs__(self):
        return abs(self.a + self.b)

    def __add__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.a + other.a, self.b + other.b)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)

        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)

    def __rmul__(self, other):
        return self * other

    def topolar(self):
        pass




print("Printing")
print(Complex(2,3))
print(Complex(5))
print(Complex(2, -3))
z1 = Complex(2, 3)

print("\nImag / Real")
#print(z1.imag())
#print(z1.real())
z2 = Complex(4, -2)
print("\nArithmethic")
print(z1 + z2)
print(3 + z1)
print(z1 * z2)
