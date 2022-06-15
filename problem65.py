from sympy import gcd
from math import floor
from rational import Rational

__all__ = ["get_rational", "digit_sum"]

def e_expansion(rank: int) -> list[int]:
    expansion: list[int] = [2, 1, 2]

    for n in range(2, floor(rank / 3) + 2):
        expansion.append(1)
        expansion.append(1)
        expansion.append(2 * n)

    while len(expansion) > rank:
        expansion.pop()

    return expansion

def get_rational(rank: int, expansion: list[int]) -> int:
    t = Rational(1, expansion[-1])

    for i in range(len(expansion) - 2, -1, -1):
        t = expansion[i] + t
        t = 1 / t
    
    return t.invert()
        
def digit_sum(n: int) -> int:
    out = 0

    while n > 0:
        out += (n % 10)
        n //= 10

    return out

if __name__ == "__main__":
    expansion: list[int] = e_expansion(100)
    result = get_rational(100, expansion)
    numerator = result.numerator

    print(digit_sum(numerator))