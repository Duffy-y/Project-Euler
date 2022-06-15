
def fib(n_minus_1, n_minus_2) -> int:
    return n_minus_1 + n_minus_2

def contains_n_digits(number, n: int) -> bool:
    if 1 <= number / 10**(n-1) <= 9.9:
        return True
    return False

n_1 = 1
n_2 = 1
i = 2

while not contains_n_digits(n_2, 1000):
    i += 1
    n_1, n_2 = n_2, fib(n_1, n_2)

print(f"n1 = {n_1} (longueur: {len(str(n_1))}) \n n2 = {n_2} (longueur: {len(str(n_2))}")
print(i)
