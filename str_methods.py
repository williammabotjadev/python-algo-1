# String Methods

slayer = ["Buffy", "Anne", "Summers"]

res = " ".join(slayer)

print(res)

res = "--<->--".join(slayer)

print(res)

res = "".join(slayer)

print(res)

res = "".join(reversed(slayer))

print(res)

name = "Mr. Anderson"
movie = "The Matrix"

print(name.ljust(50, "*"))
print(movie.rjust(50, "#"))