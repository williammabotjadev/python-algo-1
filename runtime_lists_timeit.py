# Benchmarking runtime Lists with timeit module

def test():
    l = []
    for i in range(1000):
        l = l + [i]

def test_one():
    l = []
    for i in range(1000):
        l.append(i)

def test_two():
    l = []
    l = [i for i in range(1000)]

def test_three():
    l = list(range(1000))

if __name__ == "__main__":
    import timeit 
    t1 = timeit.Timer("test()", "from __main__ import test")
    print("Concatenation", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer("test_one()", "from __main__ import test_one")
    print("Append", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer("test_two()", "from __main__ import test_two")
    print("Comprehension", t3.timeit(number=1000), "milliseconds")
    t4 = timeit.Timer("test_three()", "from __main__ import test_three")
    print("Type Casting Range", t4.timeit(number=1000), "milliseconds")
    