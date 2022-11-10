# Passing starred arguments to a Function

def mult(a, b, c):
    return a * b * c

if __name__ == "__main__":
    L = [1,2,3]
    print(mult(*L))