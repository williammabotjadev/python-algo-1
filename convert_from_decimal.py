# Convert from a Decimal

def convert_to_decimal(num, base):
    
    mult, res = 1, 0

    while num > 0:
        res += num % base * mult 
        mult *= 10 
        num = num // base
    return res 

def test():
    number, base = 9, 2
    assert(convert_to_decimal(number, base) == 1001)
    print("Test Passed!")

if __name__ == "__main__":
    test()
