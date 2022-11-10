# Finding Greatest Common Divisor

def finding_gcd(a, b):
    """ An Implementation to find the Greatest Common Divisor"""
    while(b != 0):
        result = b 
        a, b = b, a % b 
    return result 

def test():
    x, y = 21, 12
    m, n = 49, 7
    assert(finding_gcd(x, y) == 3)
    assert(finding_gcd(m, n) == 7)
    print("Test Passed")

if __name__ == "__main__":
    test()