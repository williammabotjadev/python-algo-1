# Set Operations with Dictionaries
 
from collections import OrderedDict

def set_ops_with_dict():
    pairs = [('a', 1), ('b', 2), ('c', 3)]
    d_one = OrderedDict(pairs)
    print(d_one)

    d_two = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

    print(d_two)

    union_keys = d_one.keys() & d_two.keys()
    print(union_keys)

    union_items = d_one.items() & d_two.items()
    print(union_items)

    sub_keys_one = d_one.keys() - d_two.keys()  
    print(sub_keys_one)

    sub_keys_two = d_two.keys() - d_one.keys()
    print(sub_keys_two)

    sub_items = d_one.items() - d_two.items()
    print(sub_items)

    d_three = {key:d_two[key] for key in d_two.keys() - {'c', 'd'}}
    print(d_three)

if __name__ == "__main__":
    set_ops_with_dict()