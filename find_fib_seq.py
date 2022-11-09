# Finding the Fibonacci Sequence in 3 different ways

import math 

# Using Iteration

def find_fib_iter(n):
    if n < 2:
        return n

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
    return a

# Using Recursion

def find_fib_rec(n):
    if n < 2:
        return n 
    return find_fib_rec(n - 1) + find_fib_rec(n - 2)

# Using a Formula 

def find_fib_form(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    return int(math.floor(phi ** n / sqrt5))


def test():
    n = 10
    assert(find_fib_form(n) == 55)
    assert(find_fib_iter(n) == 55)
    assert(find_fib_rec(n) == 55)
    print("Test Passed")

if __name__ == "__main__":
    test()