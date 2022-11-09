# Convert between different bases

def convert_to_decimal(num, base):
    
    mult, res = 1, 0

    while num > 0:
        res += num % 10 * mult 
        mult *= base 
        num = num // 10
    return res 

def test():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("Test Passed!")

if __name__ == "__main__":
    test()
