from re import I

from numpy import square


def sum_of_square(n: int) -> int:
    total: int = 0
    for i in range(1, n + 1):
        total += i**2
    return total

def square_of_sum(n: int) -> int:
    total: int = 0
    for i in range(1, n + 1):
        total += i
    return total ** 2

def difference(n: int) -> int:
    return square_of_sum(n) - sum_of_square(n)

print(difference(100))