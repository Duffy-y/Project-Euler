from math import ceil, sqrt


from numpy import iinfo


def count_divisor(n: int) -> int:
    count: int = 0
    for divisor in range(1, ceil(sqrt(n))):
        if n % divisor == 0:
            count += 2
    return count

i: int = 2
triangle_number: int = 1
found: bool = False

while not found:
    print(f"Searching for {triangle_number}")
    if count_divisor(triangle_number) >= 500:
        found = True
        break
    triangle_number += i
    i += 1

print(f"First triangle number to have over 500 divisors is {triangle_number}")