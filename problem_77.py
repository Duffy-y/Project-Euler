from turtle import update
import sympy as sp
from typing import List
    
class PrimeSolver(object):
    def __init__(self):
        self.prime_list: List[int] = []
        self.prime_length: int = 0
        self.total_ways: int = 0
        self.n: int = 0
    
    def initialize(self, n_start: int) -> None:
        self.n = n_start
        self.total_ways = 0
        self.prime_list: List[int] = list(sp.primerange(0, n_start))
        self.prime_length: int = len(self.prime_list)
        
    def solve(self, n_start: int) -> int:
        self.initialize(n_start)
        
        is_found = False
        while not is_found:
            self.update_prime_list()
            
            for prime in self.prime_list:
                self.count_sequences(prime, prime, prime) 
            
            if self.total_ways >= 5000:
                print(f"NUMBER FOUND ! n = {self.n}")
                break;
            else:
                self.total_ways = 0
            
            self.n += 1
            
    def solve_unique(self, n: int) -> int:
        self.initialize(n)
        
        for prime in self.prime_list:
            self.count_sequences(prime, prime, prime) 
            
        print(self.total_ways)
        
    def count_sequences(self, sum: int, base_sum_integer: int, str_sum) -> int:
        if sum > self.n:
            return 0
        if sum == self.n:
            # print(str_sum)
            self.total_ways += 1
            return 0
        
        for i in self.prime_list:
            if base_sum_integer > i:
                continue
            
            self.count_sequences(sum + i, i, f"{str_sum} + {i}")
             
    def update_prime_list(self) -> None:
        last_prime = self.prime_list[-1]
        next_prime = PrimeSolver.get_next_prime_number(last_prime)
        
        if next_prime < self.n:
            self.prime_list.append(next_prime)
            self.prime_length += 1
       
    @staticmethod     
    def get_next_prime_number(n: int) -> int:
        """
        Get the next prime number after n.
        """
        return int(sp.nextprime(n))

prime_solver = PrimeSolver()
prime_solver.solve(10)
