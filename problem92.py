import numpy as np
import sys
from enum import Enum

from tqdm import tqdm

def next_number(n: int) -> int:
    out = 0

    while n > 0:
        out += (n % 10) ** 2
        n //= 10

    return out

def end_with_89(n: int) -> bool:
    while n != 89 and n != 1:
        n = next_number(n)
    return n == 89

count = 0
known_nodes = {}

for i in tqdm(range(1, 10_000_000 + 1)):
    res = end_with_89(i)
    if res:
        count += 1

print(count)