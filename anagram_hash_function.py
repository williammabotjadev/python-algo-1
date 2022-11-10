# Finding Anagrams using Hash Function

def hash_func(astring, table_size):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])
    return sum % table_size


