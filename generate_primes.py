# Generate n number of primes

import math 
import random 
import sys 

from find_if_prime import finding_prime_sqrt

def generate_primes(n=3):
    while 1:
        p = random.randint(pow(2, n - 2), pow(2, n - 1) - 1)
        p = 2 * p + 1
        if finding_prime_sqrt(p):
            return p 
            
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_primes.py number")
        sys.exit()
    else:
        n = int(sys.argv[1])
        print(generate_primes(n))