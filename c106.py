
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imag = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return Complex(real, imag)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            return "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary > 0:
                return "0.00+%.2fi" % self.imaginary
            else:
                return "0.00-%.2fi" % abs(self.imaginary)
        elif self.imaginary > 0:
            return "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            return "%.2f-%.2fi" % (self.real, abs(self.imaginary))
