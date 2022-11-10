# List Comprehensions

a = [y for y in range(1900, 2022) if y % 4 == 0]

print(a)

b = [2**i for i in range(13)]

print(b)

c = [i for i in range(10) if i % 2 == 0]

print(c)

d = [str(round(355/113, i)) for i in range(1, 6)]

print(d)

words = "The Quick Brown Fox jumps over the lazy dog".split()

e = [[w.upper(), w.lower(), len(w)] for w in words]

for i in e:
    print(i)