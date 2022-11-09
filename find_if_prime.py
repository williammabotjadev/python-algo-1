# Find out if a Number is a Prime, 3 different ways

import math 
import random 

def finding_prime(n):
    
    num = abs(n)

    if num < 4:
        return True 
    for x in range(2, num):
        if num % x == 0:
            return False 
    return False 

