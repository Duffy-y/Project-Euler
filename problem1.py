def sum_of_multiples_of_3(limit: int) -> int:
    total: int = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
    
print(sum_of_multiples_of_3(1000))