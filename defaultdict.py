# defaultdict collection example 

from collections import defaultdict

def defaultdict_example():
    pairs = {
        ('a', 1),
        ('b', 2),
        ('c', 3),
        ('d', 4)
    }

    d_one = {}

    for k, v in pairs:
        if k in d_one:
            d_one[k].append(v)
        d_one[k] = []
    print(d_one)

    d_two = defaultdict(list)

    for k, v in pairs:
        d_two[k].append(v)
    print(d_two)

if __name__ == "__main__":
    defaultdict_example()