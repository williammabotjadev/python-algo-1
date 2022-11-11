# Merge two sorted sequences with heapq module 

import heapq 

def merge_sorted_seqs(a, b):
    result = []

    for i in heapq.merge(a, b):
        result.append(i)
    return result 

if __name__ == "__main__":
    a = sorted(list(range(10)))
    b = sorted(list(range(11, 20)))

    print(merge_sorted_seqs(a, b))