from math import ceil, sqrt, floor
import itertools

def ith_digit(n: int, i: int) -> int:
    return floor(n / 10**(i - 1)) % 10

def is_prime(n: int) -> bool:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def prime_family(n:int, index_to_replace, show: bool = False):
    for index in index_to_replace:
        n -= ith_digit(n, index) * 10**(index - 1)

    prime_count = 0
    for i in range(0, 10):
        number = n
        for index in index_to_replace:
            number += i * 10**(index - 1)
        
        if is_prime(number):
            if show:
                print(number)
            prime_count += 1
    return prime_count

def generate_each_combination(length, first_index=None):
    comb = list(range(1, length + 1))

    for i in comb:
        

    return comb

def main():

    pass

main()
