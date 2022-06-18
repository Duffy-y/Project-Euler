from math import factorial

def number_of_ways(size):
    return factorial(2 * size) // (factorial(size) ** 2)

print(number_of_ways(20))