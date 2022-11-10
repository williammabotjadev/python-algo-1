# OrderedDict Collection example 

from collections import OrderedDict

def ordereddict_example():
    pairs = [
        ('a', 1),
        ('b', 2),
        ('c', 3),
        ('d', 4)
    ]

    d_one = {}

    for k, v in pairs:
        if k not in d_one:
            d_one[k] = []
        d_one[k].append(v)

    for k in d_one:
        print(k, d_one[k])

    d_two = OrderedDict(pairs)

    for k in d_two:
        print(k, d_two[k])

if __name__ == "__main__":
    ordereddict_example()