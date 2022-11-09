# Lists are Mutable

l = [1,2,3]
m = [4, l, 6]

m[0].append("Hello")

print(l)
print(m)