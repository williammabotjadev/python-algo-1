# Set Operations with Lists

# Return list with Duplicates removed 

def difference(l):
    return list(set(l))

# Return the intersection of two lists

def intersection(a, b):
    return list(set(a) & set(b))

# Return the union of two lists

def union(a, b):
    return list(set(a) | set(b))

def tests():
    list_one = [1,2,3,4,5,9,11,15]
    list_two = [4,5,6,7,8]
    list_three = []

    assert(difference(list_one) == [1, 2, 3, 4, 5, 9, 11, 15])
    assert(difference(list_two) == [4, 5, 6, 7, 8])
    assert(intersection(list_one, list_two) == [4,5])
    assert(union(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15])
    assert(difference(list_three) == [])
    assert(intersection(list_three, list_two) == list_three)
    assert(sorted(union(list_three, list_two)) == sorted(list_two))
    print("Test Passed!")

if __name__ == "__main__":
    tests()


