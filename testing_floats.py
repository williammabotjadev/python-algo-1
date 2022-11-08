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
