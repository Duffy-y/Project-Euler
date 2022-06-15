def right_rotation(n: int) -> int:
    n_str: str = str(n)
    return int(n_str[-1] + n_str[:-1])

def is_valid(n: int) -> tuple[bool, int, int]:
    rotation = right_rotation(n)
    product = rotation // n
    return (rotation % n == 0, rotation, product)

test_number: int = 142857

for n in range(100_000_000, 1_000_000_000):
    valid, rotation, prod = is_valid(n)
    if valid:
        print(f"{n} is valid | Info: {rotation} = {prod} x {n}")