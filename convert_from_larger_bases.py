# Convert from bases larger than 10

def convert_from_larger_base(num, base):
    
    strings = "0123456789ABCDEFGHIJ"
    res = ""
    while num > 0:
        digit = num % base
        res = strings[digit] + res 
        num = num // base 
    return res 

def test():
    number, base = 31, 16
    assert(convert_from_larger_base(number, base) == '1F')
    print("Test Passed!")

if __name__ == "__main__":
    test()
