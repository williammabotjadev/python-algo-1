# NamedTuple Example 

from collections import namedtuple

def namedtuple_example():
    Slayer = namedtuple('Slayer', ['location', 'weapon'])
    blade = Slayer('Los Angeles', 'Sword')
    print(blade)

if __name__ == "__main__":
    namedtuple_example()