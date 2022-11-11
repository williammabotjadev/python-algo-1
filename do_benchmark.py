# Decorators

import random 

def do_benchmark(func):
    import time 
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(f"{func.__name__} {time.time() - t}")
        return res 
    return wrapper

@do_benchmark
def random_tree(n):
    temp = [i for i in range(n)]
    for i in range(n + 1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp 

if __name__ == "__main__":
    print(random_tree(1000))