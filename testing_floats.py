# Testing Floats using Fraction and round

from fractions import Fraction

def rounding_floats(num, places):
    return round(num, places)

def float_to_fraction(num):
    return Fraction(*num.as_integer_ratio())

def get_denominator(num_one, num_two):
    a = Fraction(num_one, num_two)
    return a.denominator 

def get_numerator(num_one, num_two):
    a = Fraction(num_one, num_two)
    return a.numerator 

print(rounding_floats(3.144542524, 2))
print(float_to_fraction(3.33))
print(get_denominator(4, 3))
print(get_numerator(2, 3))

def test_testing_floats(module_name='this module'):
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number6 = 6
    assert(rounding_floats(number1, number2) == 1.2)
    assert(rounding_floats(number1*10, number3) == 10)
    assert(float_to_fraction(number1) == number4)
    assert(get_denominator(number2, number6) == number6)
    assert(get_numerator(number2, number6) == number2)

    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_testing_floats()
