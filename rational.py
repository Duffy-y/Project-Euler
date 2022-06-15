from sympy import gcd

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def __str__(self):
        self.reduce()
        res: float = float(self.numerator) / float(self.denominator)
        if res.is_integer():
            return f"{self.numerator}/{self.denominator} = {self.numerator / self.denominator}"
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Rational):
            old_denominator: int = self.denominator
            
            self.numerator *= other.denominator
            self.denominator *= other.denominator
            other.denominator *= old_denominator
            other.numerator *= old_denominator

            out = Rational(self.numerator + other.numerator, self.denominator)
            out.reduce()
            return out
        else:
            out = Rational(self.numerator + self.denominator * other, self.denominator)
            out.reduce()
            return out

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Rational):
            other.numerator *= -1
            return self + other
        else:
            return self + (-other)

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        if isinstance(other, Rational):
            out = Rational(self.numerator * other.numerator, self.denominator * other.denominator)
            out.reduce()
            return out
        else:
            out = Rational(self.numerator * other, self.denominator)
            out.reduce()
            return out

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Rational):
            out = Rational(self.numerator * other.denominator, self.denominator * other.numerator)
            out.reduce()
            return out
        else:
            out = Rational(self.numerator, self.denominator * other)
            out.reduce()
            return out

    def __rtruediv__(self, other):
        if isinstance(other, Rational):
            out = Rational(other.numerator * self.denominator, other.denominator * self.numerator)
            out.reduce()
            return out
        else:
            out = Rational(other * self.denominator, self.numerator)
            out.reduce()
            return out

    def __itruediv__(self, other):
        return self / other

    def reduce(self):
        common_factor = gcd(self.numerator, self.denominator)
        self.numerator /= common_factor
        self.denominator /= common_factor

    def invert(self):
        self.numerator, self.denominator = self.denominator, self.numerator
        self.reduce()
        return self

    def __eq__(self, other):
        other.reduce()
        self.reduce()
        return self.numerator == other.numerator and self.denominator == other.denominator