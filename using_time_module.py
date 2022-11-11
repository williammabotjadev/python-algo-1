# Using time module, Unit testing

import time 

def sumofn2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
         theSum += i 

    end = time.time()

    return theSum, end - start 

if __name__ == "__main__":
    n = 5 
    print(f"The sum is {sumofn2(n)}")
    n = 200 
    print(f"The sum is {sumofn2(n)}")

