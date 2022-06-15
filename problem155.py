from rational import Rational
from math import floor
from itertools import *
from itertools import chain
from tqdm import tqdm
from numpy import gcd

if __name__ == "__main__":
    limit = 18
    possible_value = [[], [(1, 1)]]
    set_poss = set({(1, 1)})

    for m in range(2, limit + 1):
        print(f"Generating every way for n={m} capacitors")
        m_value = set()

        for k in range(1, m//2 + 1):
            for (num1, denum1) in possible_value[k]:
                for (num2, denum2) in possible_value[m - k]:
                    num_prod = num1 * num2
                    denum_prod = denum1 * denum2
                    sum = num1 * denum2 + num2 * denum1
                    series_gcd = gcd(num_prod, sum)
                    parallel_gcd = gcd(sum, denum_prod)
                    series = (num_prod // series_gcd, sum // series_gcd)
                    parallel = (sum // parallel_gcd, denum_prod // parallel_gcd)
                    m_value.add(series)
                    m_value.add(parallel)

        possible_value.append(m_value)
        set_poss.update(m_value)
    print(f"There is exactly {len(set_poss)} unique ways with {limit} capacitors")

    

