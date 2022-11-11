# Filter Method

def f(i):
    return i % 2 != 0 or i % 3 != 0

list_col = [1, 15, 3, 17, 41, 49, 20]

res = filter(f, list_col)
print(next(res))
print(next(res))
print(next(res))