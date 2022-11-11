# Map Method

def cube(i):
    return i * i * i 

def square(i):
    return i * i 

res_one = map(cube, range(2000, 2022))

for i in range(2000, 2022):
    print(res_one.__next__())

seq = range(8)

res_two = map(None, seq, map(cube, seq))

print(res_two)