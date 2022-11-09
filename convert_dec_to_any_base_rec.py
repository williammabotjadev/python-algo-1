# Convert any Decimal to any Base using Recursion

def convert_dec_to_any_base_rec(num, base):
    """Convert an Integer to any Base String"""
    strings = "0123456789ABCDEF"

    if num < base:
        return strings[num]
    else:
        return convert_dec_to_any_base_rec(num//base, base) + strings[num % base]

def test():
    number, base = 9, 2
    assert(convert_dec_to_any_base_rec(number, base) == '1001')
    print("Test Passed!")

if __name__ == "__main__":
    test()
