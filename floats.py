# Floats

def a(x, y, places=7):
    return round(abs(x - y), places) == 0

print(a(24, 16, 4))