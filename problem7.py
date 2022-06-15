from sympy.ntheory.primetest import isprime

n: int = 1
nth_prime: int = 2
number: int = 2

while n != 10001:
    number += 1
    if isprime(number):
        n += 1
        nth_prime = number

print(f"10 001st prime number is {nth_prime}")
