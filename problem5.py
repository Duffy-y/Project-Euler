found: bool = False
n: int = 1

while not found:
    print(n)
    found: bool = True
    for i in range(1, 21):
        if n % i != 0:
            n += 1
            found = False

print(f"Smallest number = {n}")