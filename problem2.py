from cmath import sqrt

n_1: int = 1
n_2: int = 2
even_sum: int = 0

while n_2 < 4_000_000:
    # print(n_2)
    if n_2 % 2 == 0:
        even_sum += n_2

    n_1, n_2 = n_2, n_1 + n_2

print(f"sum: {even_sum}")