# Finding Greatest Common Divisor

def finding_gcd(a, b):
    """ An Implementation to find the Greatest Common Divisor"""
    while(b != 0):
        result = b 
        a, b = b, a % b 
    return result 

