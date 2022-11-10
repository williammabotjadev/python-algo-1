# Decorators

import random 
import time 

def do_benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(f"{func.__name__} {time.clock() - t}")
        return res 
    return wrapper

