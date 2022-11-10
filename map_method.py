# Map Method

def cube(i):
    return i * i * i 

def square(i):
    return i * i 

res_one = map(cube, range(2000, 2022))

for i in range(2000, 2022):
    print(res_one.__next__())

seq = range(8)

res_two = map(square, map(cube, seq))

for j in range(8):
    print(res_two.__next__())