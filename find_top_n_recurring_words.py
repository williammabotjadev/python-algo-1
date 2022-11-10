# Finding top N recurring words using Counter collection 

from collections import Counter

def find_top_n_words(seq, N):
    dcounter = Counter()
    for word in seq.split():
        dcounter[word] += 1 
    return dcounter.most_common(N)

def test(module_name="This Module"):
    seq = 'buffy angel monster xander a willow gg buffy the monster super buffy angel'
    N = 3 

    assert(find_top_n_words(seq, N) == [('buffy', 3), ('angel', 2), ('monster', 2)])
    print(find_top_n_words(seq, N))
    name=module_name
    con="Passed"
    output = f"The Test in {name} has {con}"
    print(output)

if __name__ == "__main__":
    test()