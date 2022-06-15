from problem64 import *
from problem65 import *
import numpy as np
from math import sqrt

def is_perfect_square(n) -> bool:
    return sqrt(n).is_integer()

def is_solution(D, fraction: Rational) -> bool:
    return fraction.numerator**2 - D * fraction.denominator**2 == 1

def _get_rational(limit: int, expansion: list[int], n: int = 1, total: int = 1) -> Rational:
    if limit == total:
        return Rational(expansion[n - 1], 1)
    else:
        return expansion[n - 1] + 1 / _get_rational(limit, expansion, 2 if n == len(expansion) else n + 1, total + 1)

def get_rational(limit: int, expansion: list[int]) -> Rational:
    return _get_rational(limit, expansion)

if __name__ == "__main__":
    max_x = -1
    max_D: int = -1
    for D in range(2, 1_001):
        if is_perfect_square(D):
            continue

        expansion = continued_fraction_flat(D)
        found = False
        rank = 1
        while not found:
            frac: Rational = get_rational(rank, expansion)
            rank += 1
            if is_solution(D, frac):
                if frac.numerator > max_x:
                    max_x = frac.numerator
                    max_D = D
                print(f"(x, y) = {(frac.numerator, frac.denominator)} is solution for D = {D} (max_D = {max_D}, max_x = {max_x})")
                found = True

    print(f"Largest x is obtained at D = {max_D}")


