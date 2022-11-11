# Merge two sorted sequences with heapq module 

import heapq 

def merge_sorted_seqs(a, b):
    result = []

    for i in heapq.merge(a, b):
        result.append(i)
    return result 

