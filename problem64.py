from math import floor, sqrt

from sympy import is_perfect

__all__ = ["continued_fraction", "continued_fraction_flat"]

def continued_fraction(N: float) -> tuple[int, list[int]]:
    if sqrt(N).is_integer():
        return None

    N_root: float = sqrt(N)
    a0: int = floor(N_root)
    a: int = a0
    r: int = 0
    s: int = 1

    continued_representation: tuple[int, list[int]] = [a, []]

    while 2 * a0 != a:
        r = a * s - r
        s = (N - r**2)/s
        a = floor((r + a0) / s)
        continued_representation[1].append(a)
    
    return continued_representation

def continued_fraction_flat(N: float) -> list[int]:
    if sqrt(N).is_integer():
        return None

    N_root: float = sqrt(N)
    a0: int = floor(N_root)
    a: int = a0
    r: int = 0
    s: int = 1

    continued_representation: list[int] = [a]

    while 2 * a0 != a:
        r = a * s - r
        s = (N - r**2)/s
        a = floor((r + a0) / s)
        continued_representation.append(a)
    
    return list(continued_representation)

def is_period_even(N: int) -> bool:
    return len(continued_fraction(N)[1]) % 2 == 0