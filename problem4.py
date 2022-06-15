def is_palindromic(n: int) -> bool:
    n_str: str = str(n)
    size: int = len(n_str)
    for i in range(size):
        if n_str[i] != n_str[size - i - 1]:
            return False
    return True

max_palindrome: int = -1
for i in range(100, 1000):
    for j in range(100, 1000):
        number: int = i * j
        if is_palindromic(number) and number > max_palindrome:
            max_palindrome = number

print(f"Largest palindrome is {max_palindrome}")