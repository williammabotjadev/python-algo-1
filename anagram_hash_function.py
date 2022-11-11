# Finding Anagrams using Hash Function

def hash_func(astring, table_size):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])
    return sum % table_size

def find_ana_hash_func(word_one, word_two):
    tablesize = 11 
    return hash_func(word_one, tablesize) == hash_func(word_two, tablesize)

def test(module_name="This Module"):
    word_one = "buffy"
    word_two = "bffyu"
    word_three = "bffya"

    assert(find_ana_hash_func(word_one, word_two) == True)
    assert(find_ana_hash_func(word_one, word_three) == False)

    name=module_name
    con="Passed"

    print(f"{name} has {con} all tests!")

if __name__ == "__main__":
    test()