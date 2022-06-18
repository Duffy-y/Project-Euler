from tqdm import tqdm

def collatz(n: int) -> int:
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def collatz_length(n: int) -> int:
    length: int = 1
    val: int = n
    while val != 1:
        val = collatz(val)
        length += 1

    return length
        
max_length: int = -1
res: int = -1
for i in tqdm(range(1, 1_000_000)):
    length = collatz_length(i)
    if max_length < length:
        max_length = length
        res = i

print(res)
        