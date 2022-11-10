# Lists are Mutable

l = [1,2,3]
m = [4, l, 6]

m[1].append("Hello")

print(l)
print(m)