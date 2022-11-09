# Finding the Fibonacci Sequence in 3 different ways

import math 

def find_fib_iter(n):
    if n < 2:
        return n

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
    return a

def find_fib_rec(n):
    if n < 2:
        return n 
    return find_fib_rec(n - 1) + find_fib_rec(n - 2)