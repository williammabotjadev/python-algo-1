# Benchmark Test for Numpy vs. Native Lists

import numpy
import time 

def trad_version():
    t_one = time.time()

    x = range(10000000)
    y = range(10000000)

    z = []

    for i in range(len(x)):
        z.append(x[i] + y[i])
    return time.time() - t_one

def numpy_version():
    t_one = time.time()

    x = numpy.arange(10000000)
    y = numpy.arange(10000000)

    z = x + y

    return time.time() - t_one 

if __name__ == "__main__":
    print(f"Traditional Lists: {trad_version()}")
    print(f"Numpy Lists: {numpy_version()}")

