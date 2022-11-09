# Find out if a Number is a Prime, 3 different ways

import math 
import random 

# Basic Approach 

def finding_prime(n):
    
    num = abs(n)

    if num < 4:
        return True 
    for x in range(2, num):
        if num % x == 0:
            return False 
    return False 

# Square Root Approach 

def finding_prime_sqrt(n):

    num = abs(n)

    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False 
    return True 

# Fermat's Theorem Approach

def finding_prime_ferm(n):
    if n <= 102:
        for a in range(2, n):
            if pow(a, n - 1, n) != 1:
                return False
        return True 
    else:
        for i in range(100):
            a = random.randint(2, n - 1)
            if pow(a, n - 1, n) != 1:
                return False 
        return True 

def test():

    num_one = 17
    num_two = 20 

    assert(finding_prime(num_one) == True)
    assert(finding_prime(num_two) == False)
    assert(finding_prime_sqrt(num_one) == True)
    assert(finding_prime_sqrt(num_two) == False)
    assert(finding_prime_ferm(num_one) == True)
    assert(finding_prime_ferm(num_two) == False)
    print("Tests Passed!")

if __name__ == "__main__":
    test()
