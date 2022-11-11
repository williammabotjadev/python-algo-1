# A Fibonacci Code that uses the Generator 

def fib_gen():
    a, b = 0, 1 
    while True:
        yield b 
        a, b = b, a + b 

if __name__ == "__main__":
    result = fib_gen()
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))